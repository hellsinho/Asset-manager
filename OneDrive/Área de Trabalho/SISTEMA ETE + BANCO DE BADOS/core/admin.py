from django.contrib import admin
from .models import HistoricoAtivacao
from .models import dados
from .models import dados1
from .models import dados2
from .models import dados3

admin.site.register(HistoricoAtivacao)
# Register your models here.
admin.site.register(dados)
admin.site.register(dados1)
admin.site.register(dados2)
admin.site.register(dados3)