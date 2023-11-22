from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.serializers import ArticleSerializer
from articles.serializers import CommentViewSerializer
from bank.serializers import DepositProductSerializer, BankSerializer
from .models import Propensity


class UserSerializer(serializers.ModelSerializer):
  article_set = ArticleSerializer(many=True, read_only=True)
  comment_set = CommentViewSerializer(many=True, read_only=True)
  like_products = DepositProductSerializer(many=True, read_only=True)
  class Meta:
    model = get_user_model()
    fields = ('username', 'article_set', 'comment_set', 'like_products',)   


class PropensitySerializer(serializers.ModelSerializer):
  user_info = UserSerializer(source='user', read_only=True)
  bank_info = BankSerializer(source='bank', read_only=True)

  class Meta:
    model = Propensity
    fields = ('id', 'user_info', 'bank_info', 'deposit_now', 'deposit_type', 'income', 'age',)
    read_only_fields = ('bank', 'user',)

class PropensityFormSerializer(serializers.ModelSerializer):
  class Meta:
    model = Propensity
    fields = ('age',)
    read_only_fields = ('bank', 'user',)

class UserInfoSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = ('id', 'username',)