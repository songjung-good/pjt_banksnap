from django.urls import path
from . import views


urlpatterns = [
  path('exchange/', views.exchange),
  path('finance/', views.finance),
  path('product/<str:type>/', views.deposit),
  path('product/detail/<int:product_id>/', views.deposit_detail),
  path('product/like/<int:product_id>/', views.product_like),
]