from django.urls import path
from . import views

app_name = 'mainpage'

urlpatterns = [
    path('home/', views.home_view, name='home'),  
    path('manage/', views.manage_view, name='manage'),  
    path('news/', views.news_view, name='news'), 
]


