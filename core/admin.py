#admin.py
from django.contrib import admin
from .models import UnidadeFloculacao, SistemaCoagulacao, UnidadePrecipitacao, TanqueAjustePH, HistoricoAtivacao

# Registre os modelos no admin
admin.site.register(UnidadeFloculacao)
admin.site.register(SistemaCoagulacao)
admin.site.register(UnidadePrecipitacao)
admin.site.register(TanqueAjustePH)
admin.site.register(HistoricoAtivacao)
