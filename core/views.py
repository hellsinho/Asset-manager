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


from django.utils import timezone  # Importe a biblioteca timezone

@login_required
def controlarHistorico_view(request):
    if not HistoricoAtivacao.objects.exists():
        # Criação de exemplos de registros fictícios com descrições de ações amigáveis
        exemplos = [
            {'ativo': 'Floculação', 'acao': 'Ativado'},
            {'ativo': 'Coagulação', 'acao': 'Desativado'},
            {'ativo': 'Precipitação', 'acao': 'Ativado'},
            {'ativo': 'Ajuste de pH', 'acao': 'Desativado'},
        ]

        for exemplo in exemplos:
            HistoricoAtivacao.objects.create(
                ativo=exemplo['ativo'],
                acao=exemplo['acao'],
                usuario=request.user,
                data=timezone.now()
            )

    historico = HistoricoAtivacao.objects.all()

    # Dicionário de mapeamento de nomes de ativos para descrições amigáveis
    descricao_ativos = {
        'floculacao': 'Unidade de Floculação',
        'coagulacao': 'Sistema de Coagulação',
        'precipitacao': 'Unidade de Precipitação',
        'ajuste-pH': 'Tanque de Ajuste de pH',
    }

    # Atualiza os nomes dos ativos com as descrições amigáveis
    for acao in historico:
        acao.ativo = descricao_ativos.get(acao.ativo, acao.ativo)

    return render(request, 'dashboard/Controlar/dashboardHistorico.html', {'historico': historico})


@login_required
def analisar_view(request):
    return render(request, 'dashboard/Analisar/dashboardAnalise.html')

@login_required
def filtroseaeradores_view(request):
    return render(request, 'dashboard/FiltroAeradores/filtros.e.aeradores.html')

@login_required
def armazenamento_view(request):
    return render(request, 'dashboard/Armazenamento/dashboardarmazenamento.html')

@login_required
def gradeamento_view(request):
    return render(request, 'dashboard/Gradeamento/dashboardgradeamento.html')

@login_required
def sedimentacao_view(request):
    return render(request, 'dashboard/Sedimentacao_coleta/sedimentacao.html')

import json
import time  # Importe a biblioteca time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import HistoricoAtivacao

@csrf_exempt
@login_required
def registra_historico(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        data = json.loads(request.body)
        ativo = data.get('ativo')
        acao = data.get('acao')
        usuario = request.user if request.user.is_authenticated else None

        if ativo and acao:
            # Registra a ação no histórico imediatamente
            HistoricoAtivacao.objects.create(ativo=ativo, acao=acao, usuario=usuario)

            # Se a ação for "Ativado", espere 10 segundos e registre automaticamente a desativação
            if acao == "Ativado":
                time.sleep(10)  # Espera por 10 segundos
                HistoricoAtivacao.objects.create(ativo=ativo, acao="Desativado automaticamente", usuario=None)

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Dados inválidos.'})
    else:
        return JsonResponse({'success': False, 'error': 'Método inválido.'})


