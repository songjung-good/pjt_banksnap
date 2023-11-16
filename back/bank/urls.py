from django.urls import path
from . import views

app_name='bank'
urlpatterns = [
  path('exchange/', views.exchange, name='exchange'),
  path('finance/', views.finance, name='finance'),
  path('product/<str:type>/', views.deposit, name='deposit'),
]