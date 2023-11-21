from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer, PropensitySerializer, PropensityFormSerializer
from bank.models import Bank
from .models import Propensity
import json


@api_view(['GET'])
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    user_serializer = UserSerializer(person)
    return Response(user_serializer.data)

@api_view(['GET', 'PUT', 'POST'])
def propensity(request):
    if request.method == 'GET':
        propensity = Propensity.objects.get(user=request.user)
        propensity_serializer = PropensitySerializer(propensity)
        return Response(propensity_serializer.data)
    elif request.method == 'POST':
        propensity_serializer = PropensityFormSerializer(data=request.data)

        if propensity_serializer.is_valid():
            print('여기까지만와줘..')
            bank = Bank.objects.get(fin_co_no=0)
            propensity_serializer.save(user=request.user, bank=bank)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        propensity = Propensity.objects.get(user=request.user)
        propensity_serializer = PropensitySerializer(propensity)
        bank = Bank.objects.get(kor_co_nm=request.data['bank_name'])
        propensity_serializer = PropensitySerializer(propensity, data=request.data)
        if propensity_serializer.is_valid():
            propensity_serializer.save(bank=bank)
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def test(request):
    bank = Bank()
    bank.fin_co_no = 000000
    bank.kor_co_nm = '미선택'
    bank.save()
    return Response({'OK':'OK'})