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

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import HistoricoAtivacao, UnidadeFloculacao, SistemaCoagulacao, UnidadePrecipitacao, TanqueAjustePH
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
@csrf_exempt
def registra_historico(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        ativo_nome = request.POST.get('ativo')
        acao = request.POST.get('acao')

        if ativo_nome and acao:
            try:
                ativo_encontrado = False
                ativos = ["UnidadePrecipitacao", "TanqueAjustePH", "SistemaCoagulacao", "UnidadeFloculacao"]

                # Verifique se o ativo está em algum tipo de ativo e registre apenas uma vez
                for tipo_ativo in ativos:
                    if ativo_nome == tipo_ativo:
                        ativo_encontrado = True
                        historico = HistoricoAtivacao.objects.create(ativo=ativo_nome, acao=acao, usuario=request.user)
                        historico.save()
                        break  # Saia do loop assim que o histórico for registrado

                if not ativo_encontrado:
                    return JsonResponse({'error': f'Nenhum ativo encontrado com o nome "{ativo_nome}".'}, status=400)

                return JsonResponse({'message': 'Histórico registrado com sucesso!'})

            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Parâmetros ausentes.'}, status=400)

    return JsonResponse({'error': 'Método inválido ou não é uma solicitação AJAX.'}, status=400)
@login_required
def controlarHistorico_view(request):
    # Recupere o histórico para cada tipo de ativo
    historico_ajuste_pH = HistoricoAtivacao.objects.filter(ativo="TanqueAjustePH")
    historico_precipitacao = HistoricoAtivacao.objects.filter(ativo="UnidadePrecipitacao")
    historico_coagulacao = HistoricoAtivacao.objects.filter(ativo="SistemaCoagulacao")
    historico_floculacao = HistoricoAtivacao.objects.filter(ativo="UnidadeFloculacao")

    return render(request, 'dashboard/Controlar/dashboardHistorico.html', {
        'historico_ajuste_pH': historico_ajuste_pH,
        'historico_precipitacao': historico_precipitacao,
        'historico_coagulacao': historico_coagulacao,
        'historico_floculacao': historico_floculacao,
    })

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

