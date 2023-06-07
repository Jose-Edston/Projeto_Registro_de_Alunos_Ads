from django.shortcuts import render, redirect, get_object_or_404
import cadastro
from . models import Cadastro
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(redirect_field_name='login')
def index(request):
    cadastro = Cadastro.objects.filter(usuario_id=request.user.id).order_by('-id')
    return render(request, 'pages/index.html', {'cadastro': cadastro})

@login_required(redirect_field_name='login')
def ver_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'pages/ver_usuarios.html', {'cadastro':cadastro})

def search(request):
    q = request.GET.get('search')
    cadastro = Cadastro.objects.filter(nome__icontains=q)
    return render(request, 'pages/index.html', {'cadastro':cadastro})

def detalhes(request, id):
    # contato = Contatos.objects.get(id=id)
    cadastro = get_object_or_404(Cadastro, id=id)
    return render(request, 'pages/detalhes.html', {'cadastro':cadastro})

def deletar(request, id):
    cadastro = Cadastro.objects.get(id=id)
    cadastro.delete()
    return redirect('index')

def adicionar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        telefone_emergencia = request.POST.get('telefone_emergencia')
        altura = request.POST.get('altura')
        historico_familiar = request.POST.get('historico_familiar')
        data_nascimento = request.POST.get('data_nascimento')
        if descricao == '':
            descricao = gerarDescricao(nome)
            
        data = request.POST.get('data_nasc')
        telefone = request.POST.get('telefone')
        imagem = request.FILES.get('imagem')
        print(imagem)
        novo_cadastro = Cadastro(usuario_id=request.user.id, nome=nome,cpf=cpf, email=email, altura=altura, descricao=descricao, historico_familiar=historico_familiar, data_nascimento=data, telefone=telefone, telefone_emergencia=telefone_emergencia, imagem=imagem, ativo=True)
        novo_cadastro.save()
        return redirect('index')
    else:
        return render(request, 'pages/adicionar.html')


def editar(request, id):
    Cadastro = Cadastro.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        altura = request.POST.get('altura')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data_nasc')
        telefone = request.POST.get('telefone')
        telefone_emergencia = request.POST.get('telefone_emergencia')
        historico_familiar = request.POST.get('historico_familiar')
        check = request.POST.get('check')
        if check == None:
            check = False
        else:
            check = True    
        imagem = request.FILES.get('imagem')
        print(imagem)
        cadastro.nome = nome
        cadastro.cpf = cpf
        cadastro.email = email
        cadastro.telefone = telefone
        cadastro.telefone_emergencia = telefone_emergencia
        cadastro.data = data
        cadastro.historico_familiar = historico_familiar
        if imagem != None:
            cadastro.imagem = imagem
        cadastro.altura = altura
        cadastro.descricao = descricao
        cadastro.ativo = check
        cadastro.save()
        return redirect('index')
    else:    
        return render(request, 'pages/editar.html', {'cadastro':cadastro})




# Create your views here.
def index(request):
    return render(request, 'pages/index.html')