from django.shortcuts import render

# caminho das interfaces
# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')