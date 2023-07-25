from django.contrib import admin
from django.urls import path

from core.views import index, statis, ativos, AS, ASA

urlpatterns = [
    path('', index, name='index'),
    path('statis/', statis, name='statis'),
    path('ativos/', ativos, name='ativos'),
    path('ativos/statis/', AS, name='statis'),
    path('ativos/statis/ativos/', ASA, name='ASA'),
    path('admin/', admin.site.urls),
]
