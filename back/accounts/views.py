from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
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

@api_view(['GET', 'POST', 'PUT'])
def propensity(request):
    propensity = Propensity.objects.get(user=request.user)
    propensity_serializer = PropensitySerializer(propensity)
    if request.method == 'GET':
        print(propensity_serializer.data)
        return Response(propensity_serializer.data)
    
    elif request.method == 'POST':
        pass

@api_view(['GET'])
def test(request):
    propensity = Propensity()
    propensity.user = get_user_model().objects.get(pk=1)
    propensity.bank = Bank.objects.get(pk=1)
    propensity.save()
    return Response({'pass', 'pass'})