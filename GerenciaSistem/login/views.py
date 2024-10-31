from django.shortcuts import render

def index(request):
    return render(request, 'login/index.html')

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

#temporario
from django.http import JsonResponse


def loginVef(request):
    request.method = 'POST'

def loginVef(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success', 'message': 'Senha correta!'})

        else:
            return JsonResponse({'status': 'error', 'message': 'Senha incorreta!'})

    return JsonResponse({'status': 'error', 'message': 'Método inválido!'})
