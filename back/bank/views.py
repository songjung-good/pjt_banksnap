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
  url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={authkey}&searchdate={now}&data={data}'
  response = requests.get(url).json()
  
  return Response(response)