from rest_framework import serializers
from .models import DepositProduct, DepositOption, Bank


class DepositOptionSerializer(serializers.ModelSerializer):
  class Meta:
    model = DepositOption
    fields = '__all__'
    read_only_fields =('product',)


class DepositProductSerializer(serializers.ModelSerializer):
  depositoption_set = DepositOptionSerializer(many=True, read_only=True)
  kor_co_nm = serializers.CharField(source='bank.kor_co_nm', read_only=True)
  class Meta:
    model = DepositProduct
    exclude = ('like_users',)
    read_only_fields = ('bank',)


class DepositListSerializer(serializers.ModelSerializer):
  class Meta:
    model = DepositProduct
    fields = '__all__'


class BankSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bank
    fields = '__all__'
