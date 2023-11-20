from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer, CommentListSerializer, CommentSerializer
from .models import Article, Comment

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def article_list(request):
  if request.method == 'GET':
    articles = get_list_or_404(Article)
    serializer = ArticleListSerializer(articles, many=True)   
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      # serializer.save()
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)

  if request.method == 'GET':
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
  elif request.method == 'DELETE':
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  elif request.method =='PUT':
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment(request, article_pk):
  article = get_object_or_404(Article, pk=article_pk)
  if request.method == 'GET':
    comments = Comment.objects.filter(article=article)
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

@api_view(['DELETE'])
def comment_delete(request, comment_pk):
  comment = get_object_or_404(Comment, pk=comment_pk)
  comment.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)
    