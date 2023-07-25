from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')

def statis(request):
    return render(request, 'core/statis.html')

def ativos(request):
    return render(request, 'core/ativos.html')

def AS(request):
    return render(request, 'core/statis.html')

def ASA(request):
    return render(request, 'core/ativos.html')


