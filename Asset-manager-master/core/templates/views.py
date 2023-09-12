# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = "Usuário ou senha incorretos."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def ativos_view(request):
    return render(request, 'dashboard/Ativos/dashboardAtivos.html')

@login_required
def ativosEstatisticas_view(request):
    return render(request, 'dashboard/estatisticasAleatorias.html')

@login_required
def estatisticasAleatorias_view(request):
    return render(request, 'dashboard/estatisticasAleatorias.html')

@login_required
def controlar_view(request):
    return render(request, 'dashboard/Controlar/dashboardControle.html')

@login_required
def controlarHistorico_view(request):
    return render(request, 'dashboard/Controlar/dashboardHistorico.html')

@login_required
def analisar_view(request):
    return render(request, 'dashboard/Analisar/dashboardAnalise.html')

@login_required
def armazenamento_view(request):
    return render(request, 'dashboard/armazenamento/dashboardarmazenamento.html')

@login_required
def gradeamento_view(request):
    return render(request, 'dashboard/gradeamento/dashboardgradeamento.html')





