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
  url = "https://finance.naver.com/marketindex"
  res = req.urlopen(url)

  soup = BeautifulSoup(res, "html.parser")
  gold_price = soup.select_one("a.head.gold_domestic > div.head_info > span.value").string
  gasoline_price = soup.select_one("a.head.gasoline > div.head_info > span.value").string
  gold_graph = soup.select_one("#oilGoldList > li:nth-child(4) > a.graph_img > img").get("src")
  gasoline_graph = soup.select_one("#oilGoldList > li.on > a.graph_img > img").get("src")
  # print(gold_graph)
  # print()
  # print(gasoline_graph)
  # print()
  # print('금 가격 = ', gold_price)
  # print('휘발유 가격 = ', gasoline_price)
  # gold = {
  #   'name': 'gold',
  #   'graph': gold_graph,
  #   'price': gold_price
  # }
  # gasoline = 
  items = [{
    'name': '금',
    'graph': gold_graph,
    'price': gold_price
  },
  {
    'name': '가솔린',
    'graph': gasoline_graph,
    'price': gasoline_price
  }]

  return Response(items)