from django.urls import path
from .views import novaPrinter, consultaPrinter, consultaRede, buscaPorIp, atualizar, deletar, buscaPorColuna, pegaArquivo




urlpatterns = [

    path('novo/', novaPrinter, name='novaPrinter'),
    path('lista/', consultaPrinter, name='consultaPrinter'),
    path('consulta/', consultaRede,name='consultaRede'),
    path('info/', buscaPorIp, name='buscaPorIp'),
    path('infolocal/', buscaPorColuna, name='buscaPorColuna'),
    path('atualizar/<str:id>', atualizar,name='atualizar'),
    path('deletar/<str:id>', deletar, name='deletar'),
    path('csv/', pegaArquivo, name='pegaArquivo'),

    ]