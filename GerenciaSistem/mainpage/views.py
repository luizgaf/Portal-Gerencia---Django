from django.shortcuts import render

@login_required
def home_view(request):
    return render(request, 'mainpage/home.html')