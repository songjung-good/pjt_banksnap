from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.serializers import ArticleSerializer
from articles.serializers import CommentViewSerializer
from bank.serializers import DepositProductSerializer


class UserSerializer(serializers.ModelSerializer):
  article_set = ArticleSerializer(many=True, read_only=True)
  comment_set = CommentViewSerializer(many=True, read_only=True)
  like_products = DepositProductSerializer(many=True, read_only=True)
  class Meta:
    model = get_user_model()
    fields = '__all__'    
