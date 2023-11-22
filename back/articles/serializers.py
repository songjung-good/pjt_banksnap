from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'content','created_at', 'updated_at', 'username',)
        read_only = ('user',)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)


class CommentListSerializer(serializers.ModelSerializer):
    # user_info = UserSerializer(source='user', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only = ('user',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)
        read_only_fields = ('user', 'article',)        


class CommentViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only = ('user',)