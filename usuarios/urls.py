from unicodedata import name
from django.urls import path

from . import views


urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('cria/post', views.criapost, name='criapost'),
    path('deleta/<int:materia_id>', views.deleta_materia, name='deleta_materia'),
    path('edita/<int:materia_id>', views.edita_materia, name='edita_materia'),
    path('atualiza_materia', views.atualiza_materia, name='atualiza_materia')

]
