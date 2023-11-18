from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from articles.models import Article
from articles.serializers import ArticleListSerializer
from django.shortcuts import get_object_or_404, get_list_or_404
# Create your views here.\
@api_view(['GET'])
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    user_serializer = UserSerializer(person)
    articles = Article.objects.filter(user=person)
    articles_serializer = ArticleListSerializer(articles, many=True)
    context = {
        'user': user_serializer.data,
        'articles': articles_serializer.data
    }

    return Response(context)