from datetime import datetime
from subprocess import DETACHED_PROCESS
from urllib.request import Request
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from Blog.models import Materia
# Create your views here.


def cadastro(request):

    if request.method == 'POST':

        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if campo_vazio(email):
            messages.error(request, 'O campo e-mail não pode ficar em branco')

            return redirect('cadastro')
        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As Senhas não são iguais')
            return redirect('cadastro')

        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuario ja cadastrado, faça seu Login!')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuario ja cadastrado, faça seu Login!')
            return redirect('login')
        user = User.objects.create_user(
            username=nome, email=email, password=senha)
        user.save()

        messages.success(request, 'usuario cadastrado com sucesso')
        return redirect('login')
    return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':

        email = request.POST['email']
        senha = request.POST['senha']

        if email == "" or senha == "":
            messages.error(
                request, 'O campo nome/email não pode ficar em branco')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list(
                'username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            messages.error(request, 'Login ou Senha invalidos!')

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        materias = Materia.objects.order_by('-data_materia').filter(pessoa=id)

        dados = {
            'materias': materias
        }
        return render(request, 'usuarios/dashboard.html', dados)

    else:
        return redirect('index')


def criapost(request):

    if request.method == 'POST':
        nome_materia = request.POST['nome_materia']
        resumo = request.POST['resumo']
        materia = request.POST['materia']
        categoria = request.POST['categoria']
        foto = request.FILES['foto_materia']
        user = get_object_or_404(User, pk=request.user.id)
        materia = Materia.objects.create(
            pessoa=user, nome_materia=nome_materia, resumo=resumo, categoria=categoria, foto=foto)
        materia.save()

        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_post.html')


def deleta_materia(request, materia_id):
    materia = get_object_or_404(Materia, pk=materia_id)
    materia.delete()
    return redirect('dashboard')


def edita_materia(request, materia_id):
    materia = get_object_or_404(Materia, pk=materia_id)
    receita_a_editar = {'materia': materia}
    return render(request, 'usuarios/editar.html', receita_a_editar)


def atualiza_materia(request):
    if request.method == 'POST':
        materia_id = request.POST['materia_id']
        r = Materia.objects.get(pk=materia_id)
        r.nome_materia = request.POST['nome_materia']
        r.resumo = request.POST['resumo']
        r.materia = request.POST['materia']
        r.categoria = request.POST['categoria']
        if 'foto_materia' in request.FILES:
            r.foto = request.FILES['foto_materia']
        r.save()
    return redirect('dashboard')


def campo_vazio(campo):

    return not campo.strip()


def senhas_nao_sao_iguais(senha, senha2):

    return senha != senha2
