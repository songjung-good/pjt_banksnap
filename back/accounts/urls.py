from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.profile),
    path('propensity/', views.propensity),
    path('test/', views.test),
]