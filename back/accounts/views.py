from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import UserSerializer, PropensitySerializer
from bank.models import Bank
from .models import Propensity
import json


@api_view(['GET'])
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    user_serializer = UserSerializer(person)
    return Response(user_serializer.data)

@api_view(['GET', 'PUT'])
def propensity(request):
    propensity = Propensity.objects.get(user=request.user)
    propensity_serializer = PropensitySerializer(propensity)
    if request.method == 'GET':
        return Response(propensity_serializer.data)
    elif request.method == 'PUT':
        bank = Bank.objects.get(kor_co_nm=request.data['bank_name'])
        propensity_serializer = PropensitySerializer(propensity, data=request.data)
        if propensity_serializer.is_valid():
            propensity_serializer.save(bank=bank)
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def test(request):
    banks = Bank.objects.all()
    for bank in banks:
        print(bank.kor_co_nm, end='", "')
    
    return Response({'OK':'OK'})