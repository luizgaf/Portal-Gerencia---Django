from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('v', views.loginVef, name='login_verifier')
]