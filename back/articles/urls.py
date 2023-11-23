from django.urls import path
from . import views

urlpatterns = [
  path('', views.article_list),
  path('<int:article_pk>/', views.article_detail),
  path('comments/<int:article_pk>/', views.comment),
  path('comment/delete/<int:comment_pk>/', views.comment_delete)
]