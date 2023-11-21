from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view
import datetime
import requests
from django.conf import settings
from .serializers import DepositProductSerializer, DepositOptionSerializer, BankSerializer
from .models import DepositProduct, DepositOption, Bank

from bs4 import BeautifulSoup
import urllib.request as req
from selenium import webdriver

@api_view(['GET'])
def exchange(request):
  authkey = settings.EXCHANGE_KEY
  # now = datetime.datetime.now().strftime("%Y%m%d")
  now = 20231117
  data = 'AP01'
  URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
  params = {
    'authkey': authkey,
    'searchdate': now,
    'data': data,
  }
  response = requests.get(URL, params).json()
  
  return Response(response)

@api_view(['GET'])
def finance(request):
  authkey = settings.FINANCE_KEY
  DP_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
  SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'
  params = {
        'auth': authkey,
        'topFinGrpNo': '020000',
        'pageNo': 1
        }
  
  financial_products = []

  # 정기예금 목록 저장
  response = requests.get(DP_URL, params=params).json()
  baseList = response.get('result').get('baseList')   # 상품 목록
  optionList = response.get('result').get('optionList')

  for product in baseList:
    if DepositProduct.objects.filter(fin_prdt_cd=product.get('fin_prdt_cd')).exists():
      continue
    if not Bank.objects.filter(fin_co_no=product.get('fin_co_no')).exists():
      bank_serializer = BankSerializer(data=product)
      if bank_serializer.is_valid():
        bank = bank_serializer.save()
    else:
      bank = Bank.objects.get(fin_co_no=product.get('fin_co_no'))
    # 예금 deposit_type = 1
    product['deposit_type'] = 1
    product_serializer = DepositProductSerializer(data=product)
    
    if product_serializer.is_valid(raise_exception=True):
      product_serializer.save(bank=bank)


  for option in optionList:
        
    product = DepositProduct.objects.get(fin_prdt_cd=option.get('fin_prdt_cd'))
    if DepositOption.objects.filter(fin_prdt_cd=option.get('fin_prdt_cd'), save_trm=option.get('save_trm')).exists():
      continue
    option_serializer = DepositOptionSerializer(data=option)
    if option_serializer.is_valid(raise_exception=True):
        option_serializer.save(product=product)

  # 적금 목록 저장
  response = requests.get(SP_URL, params=params).json()
  baseList = response.get('result').get('baseList')   # 상품 목록
  optionList = response.get('result').get('optionList')

  for product in baseList:
    if DepositProduct.objects.filter(fin_prdt_cd=product.get('fin_prdt_cd')).exists():
      continue
    if not Bank.objects.filter(fin_co_no=product.get('fin_co_no')).exists():
      bank_serializer = BankSerializer(data=product)
      if bank_serializer.is_valid():
        bank = bank_serializer.save()
    else:
      bank = Bank.objects.get(fin_co_no=product.get('fin_co_no'))
    # 적금 deposit_type = 2
    product['deposit_type'] = 2
    product_serializer = DepositProductSerializer(data=product)
    if product_serializer.is_valid(raise_exception=True):
      product_serializer.save(bank=bank)

  for option in optionList:
        
    product = DepositProduct.objects.get(fin_prdt_cd=option.get('fin_prdt_cd'))
    if DepositOption.objects.filter(fin_prdt_cd=option.get('fin_prdt_cd'), save_trm=option.get('save_trm')).exists():
      continue
    option_serializer = DepositOptionSerializer(data=option)

    if option_serializer.is_valid(raise_exception=True):
        option_serializer.save(product=product)
  data = response['result']['baseList']
  return Response(data)


@api_view(['GET'])
def deposit(request, type):
  if type == 'deposit':
    depositProducts = get_list_or_404(DepositProduct, deposit_type=1)
  else:
    depositProducts = get_list_or_404(DepositProduct, deposit_type=2)
  serializer = DepositProductSerializer(depositProducts, many=True)
  # print(serializer.data[0])
  return Response(serializer.data)
  
@api_view(['GET'])
def deposit_detail(request, product_id):
  product = DepositProduct.objects.get(pk=product_id)
  serializer = DepositProductSerializer(product)
  if request.user in product.like_users.all():
    is_liked = True
  else:
    is_liked = False
  response = {
    'product': serializer.data,
    'is_liked': is_liked
  }
  # return Response(serializer.data)
  return Response(response)


@api_view(['POST', 'DELETE'])
def product_like(request, product_id):
  product = DepositProduct.objects.get(pk=product_id)
  if request.user in product.like_users.all():
    product.like_users.remove(request.user)
    is_liked = False
  else:
    product.like_users.add(request.user)
    is_liked = True
  return Response({'is_liked': is_liked})


@api_view(['GET'])
def price(request):
  
  gold_url = "https://finance.naver.com/marketindex/goldDetail.naver"
  oil_url = "https://finance.naver.com/marketindex/oilDetail.naver?marketindexCd=OIL_GSL"
  
  res = req.urlopen(gold_url)
  soup = BeautifulSoup(res, "html.parser")
  gold_graph = soup.select_one("#content > div.spot > div.flash_area > img").get("src")
  gold_prices = soup.select("#content > div.spot > div.today > p.no_today")
  gold_before_prices = soup.select("#content > div.spot > div.today > p.no_exday")
  
  gold_price = ''
  gold_before_price = ''
  for price in gold_prices:
    gold_price += price.get_text()
  
  for before_price in gold_before_prices:
    gold_before_price += before_price.get_text()
  
  res = req.urlopen(oil_url)
  soup = BeautifulSoup(res, "html.parser")
  gasoline_graph = soup.select_one("#content > div.spot > div.flash_area > img").get("src")
  gasoline_prices = soup.select("#content > div.spot > div.today > p.no_today")
  gasoline_before_prices = soup.select("#content > div.spot > div.today > p.no_exday")
  gasoline_price = ''
  gasoline_before_price = ''
  
  for price in gasoline_prices:
    gasoline_price += price.get_text()

  for before_price in gasoline_before_prices:
    gasoline_before_price += before_price.get_text()

  items = [{
    'name': '금',
    'graph': gold_graph,
    'price': gold_price,
    'before_price': gold_before_price,
  },
  {
    'name': '가솔린',
    'graph': gasoline_graph,
    'price': gasoline_price,
    'before_price': gasoline_before_price,
  }]
  # gold_url = "https://finance.naver.com/marketindex/goldDetail.naver"
  # res_gold = req.urlopen(gold_url)
  # wd = webdriver.Chrome()
  # wd.get(gold_url)
  # gold_soup = BeautifulSoup(wd.page_source, "html.parser")
  # gold_before_price = gold_soup.select("body > div > table > tbody > tr:nth-child(2) > td:nth-child(2)")
  # print(gold_before_price)

  return Response(items)