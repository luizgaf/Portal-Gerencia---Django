from django.shortcuts import render

def index(request):
    return render(request, 'login/index.html')

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


def loginVef(request):
    request.method = 'POST'

def loginVef(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            destino = reverse('mainpage:home')
            return redirect(destino)

        else:
            messages.error(request, 'Senha ou Login Incorretos')
            return render(request, 'login/index.html')

    return render(request, 'login/index.html')
