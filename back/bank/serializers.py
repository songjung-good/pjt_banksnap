from rest_framework import serializers
from .models import DepositProduct, DepositOption


class DepositProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = DepositProduct
    fields = '__all__'


class DepositOptionSerializer(serializers.ModelSerializer):
  class Meta:
      model = DepositOption
      fields = '__all__'
      read_only_fields =('product',)
