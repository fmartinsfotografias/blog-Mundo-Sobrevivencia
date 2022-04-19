from .models import Materia
from django.shortcuts import render, get_list_or_404, get_object_or_404


# Create your views here.


def index(request):

    materias = Materia.objects.order_by('-data_materia')

    dados = {
        'materias': materias,
    }

    return render(request, 'index.html', dados)


def noticia(request, noticia_id):
    materia = get_object_or_404(Materia, pk=noticia_id)

    materia_a_exibir = {

        'materias': materia

    }
    return render(request, 'noticia.html', materia_a_exibir)


def buscar(request):
    lista_materias = Materia.objects.order_by(
        '-data_materia').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_materias = lista_materias.filter(
                nome_materia__icontains=nome_a_buscar)

    dados = {
        'materias': lista_materias
    }

    return render(request, 'buscar.html', dados)
