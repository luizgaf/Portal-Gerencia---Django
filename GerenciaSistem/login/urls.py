from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('loginVef/', views.loginVef, name='login_verifier')
]