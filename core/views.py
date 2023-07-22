from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirecionar após o login bem-sucedido
        else:
            error_message = "Credenciais inválidas. Tente novamente."
            return render(request, 'core/index.html', {'error_message': error_message})

    return render(request, 'core/index.html')

@login_required
def pagina_restrita(request):
    # Código da view aqui
    return render(request, 'core/pagina_restrita.html')

def logout_view(request):
    logout(request)
    return redirect('index')  # Redirecionar após o logout
