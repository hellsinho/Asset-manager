# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Sedimentacao
from .models import dados
from .models import dados1
from .models import dados2
from .models import dados3


@login_required
def filtroseaeradores_view(request):
    Dados = dados.objects.all()
    return render(request, 'dashboard/FiltroAeradores/filtros.e.aeradores.html', {'Dados': Dados})


@login_required
def filtroseaeradores1_view(request):
    Dados1 = dados1.objects.all()
    return render(request, 'dashboard/FiltroAeradores/filtros.e.aeradores.html', {'Dados1': Dados1})

@login_required
def filtroseaeradores2_view(request):
    Dados2 = dados2.objects.all()
    return render(request, 'dashboard/FiltroAeradores/filtros.e.aeradores.html', {'Dados2': Dados2})

@login_required
def filtroseaeradores3_view(request):
    Dados3 = dados3.objects.all()
    return render(request, 'dashboard/FiltroAeradores/filtros.e.aeradores.html', {'Dados3': Dados3})

@login_required
def salvar_view(request):
    vnome = request.POST.get("nome")
    dados.objects.create( dado = vnome )
    Dados = dados.objects.all()
    return render(request, 'dashboard/FiltroAeradores/filtros.e.aeradores.html', {'Dados': Dados})

@login_required
def salvar1_view(request):
    vvnome = request.POST.get("nome1")
    dados1.objects.create( dado1 = vvnome )
    Dados1 = dados1.objects.all()
    return render(request, 'dashboard/FiltroAeradores/filtros.e.aeradores.html', {'Dados1': Dados1})

@login_required
def salvar2_view(request):
    vvvnome = request.POST.get("nome2")
    dados2.objects.create( dado2 = vvvnome )
    Dados2 = dados2.objects.all()
    return render(request, 'dashboard/FiltroAeradores/filtros.e.aeradores.html', {'Dados2': Dados2})

@login_required
def salvar3_view(request):
    vvvvnome = request.POST.get("nome3")
    dados3.objects.create( dado3 = vvvvnome )
    Dados3 = dados3.objects.all()
    return render(request, 'dashboard/FiltroAeradores/filtros.e.aeradores.html', {'Dados3': Dados3})


@login_required
def editar_view(request, id):
    DADOS = dados.objects.get(id=id)
    return render(request, 'dashboard/FiltroAeradores/update.html', {'DADOS': DADOS})

@login_required
def editar1_view(request, id):
    DADOS1 = dados1.objects.get(id=id)
    return render(request, 'dashboard/FiltroAeradores/update1.html', {'DADOS1': DADOS1})

@login_required
def editar2_view(request, id):
    DADOS2 = dados2.objects.get(id=id)
    return render(request, 'dashboard/FiltroAeradores/update2.html', {'DADOS2': DADOS2})

@login_required
def editar3_view(request, id):
    DADOS3 = dados3.objects.get(id=id)
    return render(request, 'dashboard/FiltroAeradores/update3.html', {'DADOS3': DADOS3})

@login_required
def update_view(request, id):
    vnome = request.POST.get('nome')
    DADOS = dados.objects.get(id=id)
    DADOS.dado = vnome
    DADOS.save()
    return redirect(filtroseaeradores_view)
@login_required
def update1_view(request, id):
    vvnome = request.POST.get('nome1')
    DADOS1 = dados1.objects.get(id=id)
    DADOS1.dado1 = vvnome
    DADOS1.save()
    return redirect(filtroseaeradores1_view)
@login_required
def update2_view(request, id):
    vvvnome = request.POST.get('nome2')
    DADOS2 = dados2.objects.get(id=id)
    DADOS2.dado2 = vvvnome
    DADOS2.save()
    return redirect(filtroseaeradores2_view)
@login_required
def update3_view(request, id):
    vvvvnome = request.POST.get('nome3')
    DADOS3 = dados3.objects.get(id=id)
    DADOS3.dado3 = vvvvnome
    DADOS3.save()
    return redirect(filtroseaeradores3_view)

@login_required
def delete_view(request, id):
    DADOS = dados.objects.get(id=id)
    DADOS.delete()
    return redirect(filtroseaeradores_view)

@login_required
def delete1_view(request, id):
    DADOS1 = dados1.objects.get(id=id)
    DADOS1.delete()
    return redirect(filtroseaeradores1_view)

@login_required
def delete2_view(request, id):
    DADOS2 = dados2.objects.get(id=id)
    DADOS2.delete()
    return redirect(filtroseaeradores2_view)

@login_required
def delete3_view(request, id):
    DADOS3 = dados3.objects.get(id=id)
    DADOS3.delete()
    return redirect(filtroseaeradores3_view)



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
def filtroseaeradores_view(request):
    return render(request, 'dashboard/FiltroAeradores/filtros.e.aeradores.html')

@login_required
def armazenamento_view(request):
    return render(request, 'dashboard/armazenamento/dashboardarmazenamento.html')

@login_required
def gradeamento_view(request):
    return render(request, 'dashboard/gradeamento/dashboardgradeamento.html')

@login_required
def sedimentacao_view(request):
    sedimentacao = Sedimentacao.objects.all()
    return render(request, 'dashboard/sedimentacao_coleta/sedimentacao.html', {'sedimentacao': sedimentacao})