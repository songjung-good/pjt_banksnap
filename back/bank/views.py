from django.shortcuts import render
from rest_framework.response import Response

from rest_framework.decorators import api_view
import datetime
import requests
from django.conf import settings


@api_view(['GET'])
def exchange(request):
  authkey = settings.EXCHANGE_KEY
  now = datetime.datetime.now().strftime("%Y%m%d")
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
  URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
  params = {
        'auth': authkey,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
  response = requests.get(URL, params=params).json()
  data = response['result']['baseList']
  return Response(data)