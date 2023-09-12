from django.contrib import admin
from .models import Sedimentacao
from .models import dados
from .models import dados1
from .models import dados2
from .models import dados3

# Register your models here.
admin.site.register(Sedimentacao)
admin.site.register(dados)
admin.site.register(dados1)
admin.site.register(dados2)
admin.site.register(dados3)