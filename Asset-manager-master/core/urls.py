# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('salvar/', views.salvar_view, name= "salvar"),
    path('salvar1/', views.salvar1_view, name= "salvar1"),
    path('salvar2/', views.salvar2_view, name= "salvar2"),
    path('salvar3/', views.salvar3_view, name= "salvar3"),
    path('editar/<int:id>', views.editar_view, name='editar'),
    path('editar1/<int:id>', views.editar1_view, name='editar1'),
    path('editar2/<int:id>', views.editar2_view, name='editar2'),
    path('editar3/<int:id>', views.editar3_view, name='editar3'),
    path('update/<int:id>', views.update_view, name='update'),
    path('update1/<int:id>', views.update1_view, name='update1'),
    path('update2/<int:id>', views.update2_view, name='update2'),
    path('update3/<int:id>', views.update3_view, name='update3'),
    path('delete/<int:id>', views.delete_view, name='delete'),
    path('delete1/<int:id>', views.delete1_view, name='delete1'),
    path('delete2/<int:id>', views.delete2_view, name='delete2'),
    path('delete3/<int:id>', views.delete3_view, name='delete3'),
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Página de redirecionamento após o login bem-sucedido
    path('dashboard/ativos/', views.ativos_view, name='ativos'),
    path('dashboard/ativos/estatisticasAleatorias/', views.ativosEstatisticas_view, name='ativos'),
    path('dashboard/estatisticasAleatorias/', views.estatisticasAleatorias_view, name='estatisticasAleatorias'),
    path('dashboard/filtros.e.aeradores', views.filtroseaeradores_view, name= "filtros"),
    path('dashboard/controlar', views.controlar_view, name='controlar'),
    path('dashboard/controlar/historico', views.controlarHistorico_view, name='controlarHistorico'),
    path('dashboard/analisar', views.analisar_view, name='analisar'),
    path('dashboard/armazenamento', views.armazenamento_view, name='armazenamento'),
    path('dashboard/gradeamento', views.gradeamento_view, name='gradeamento'),
    path('dashboard/sedimentacao/', views.sedimentacao_view, name='sedimentacao'),
]