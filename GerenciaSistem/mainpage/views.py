from django.shortcuts import render

def home_view(request):
    return render(request, 'mainpage/home.html')

def manage_view(request):
    return render(request, 'mainpage/manage.html')

def news_view(request):
    return render(request, 'mainpage/news.html')