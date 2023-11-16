from rest_framework import serializers
from .models import DepositProduct, DepositOption


class DepositOptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = DepositOption
    fields = '__all__'
    read_only_fields =('product',)


class DepositProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = DepositProduct
    fields = '__all__'
  deposit_option_set = DepositOptionSerializer(many=True, read_only=True)


class DepositListSerializer(serializers.ModelSerializer):
  class Meta:
    model = DepositProduct
    fields = '__all__'
