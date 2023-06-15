from django.shortcuts import render, redirect, get_object_or_404
from . models import Aluno, Nota, Turma, Frequencia
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

class ViewAluno:

    @login_required(redirect_field_name='login')
    def ver_todos_alunos(request):
        alunos = Aluno.objects.all()
        return render(request, 'pages/controle.html', {'alunos':alunos}) #TODO

    def pesquisar_aluno(request):
        try:
            q = request.GET.get('busca_aluno')
            aluno = Aluno.objects.get(numero_matricula=q)
            return render(request, 'pages/controle.html', {'aluno':aluno})
        except :
            alunos = Aluno.objects.all()
            return render(request, 'pages/controle.html', {'alunos':alunos})

    def detalhes_aluno(request, id):
        aluno = get_object_or_404(Aluno, id=id)
        return render(request, 'pages/cadastro_alunos.html', {'aluno':aluno})

    def deletar_aluno(request, id):
        aluno = Aluno.objects.get(id=id)
        aluno.delete()
        return redirect('home')

    def adicionar_aluno(request, id):
        if request.method == 'POST':
            numero_matricula = request.POST.get('matricula')
            nome = request.POST.get('nome')
            imagem = request.FILES.get('imagem')
            cpf = request.POST.get('cpf')
            email = request.POST.get('email')
            telefone = request.POST.get('telefone')
            telefone_emergencia = request.POST.get('telefone_emergencia')
            historico_familiar = request.POST.get('historico_familiar')
            data_nascimento = request.POST.get('data_nascimento')
                
            novo_aluno = Aluno(numero_matricula=numero_matricula, nome=nome,cpf=cpf, email=email, historico_familiar=historico_familiar, data_nascimento=data_nascimento, telefone=telefone, telefone_emergencia=telefone_emergencia, imagem=imagem, aprovado=True)
            novo_aluno.save()

            return redirect('home')
        else:
            return render(request, 'pages/cadastro_alunos.html')


    def editar_aluno(request, id):
        aluno = Aluno.objects.get(numero_matricula=id)
        if request.method == 'POST':
            numero_matricula = request.POST.get('matricula')
            nome = request.POST.get('nome')
            imagem = request.FILES.get('imagem')
            cpf = request.POST.get('cpf')
            email = request.POST.get('email')
            telefone = request.POST.get('telefone')
            telefone_emergencia = request.POST.get('telefone_emergencia')
            historico_familiar = request.POST.get('historico_familiar')
            data_nascimento = request.POST.get('data_nascimento')
            imagem = request.FILES.get('imagem')
            
            aluno.numero_matricula = numero_matricula
            aluno.nome = nome
            aluno.cpf = cpf
            aluno.email = email
            aluno.telefone = telefone
            aluno.telefone_emergencia = telefone_emergencia
            aluno.data_nascimento = data_nascimento
            aluno.historico_familiar = historico_familiar
            if imagem != None:
                aluno.imagem = imagem
            aluno.save()
            # TODO
            return redirect('cadastro')
        else:    
            return render(request, 'pages/cadastro_alunos.html', {'aluno':aluno})

class ViewNota:
    @login_required(redirect_field_name='login')
    def ver_todas_notas(request):
        notas = Nota.objects.all()
        return render(request, 'pages/cadastro_nota.html', {'notas':notas})


    def cadastrar_nota(request, numero_matricula):
        aluno = Aluno.objects.get(numero_matricula=numero_matricula)
        try:
            notas = Nota.objects.filter(matricula_aluno=numero_matricula)
            return render(request, 'pages/cadastro_nota.html', {'aluno':aluno, 'notas':notas})
        except:
            if request.method == 'POST':
                disciplina = request.POST.get('disciplina')
                nota_1 = request.POST.get('nota_1')
                nota_2 = request.POST.get('nota_2')
                nota_3 = request.POST.get('nota_3')
                nota_4 = request.POST.get('nota_4')
                nota_final = request.POST.get('nota_final')
                aprovado = request.POST.get('aprovado')

                nova_nota = Nota(matricula_aluno=numero_matricula, disciplina=disciplina, nota_1=nota_1, nota_2=nota_2, nota_3=nota_3, nota_4=nota_4, nota_final=nota_final)
                nova_nota.save()
                aluno.aprovado = aprovado
                aluno.save()
                print('2')
                return redirect('home')
            else:
                print('3')
                return render(request, 'pages/cadastro_nota.html', {'aluno':aluno})

class ViewFrequencia:
    @login_required(redirect_field_name='login')
    def ver_todas_frequencias(request):
        frequencias = Frequencia.objects.all()
        return render(request, 'pages/cadastro_presenca.html', {'frequencias':frequencias})


    def cadastrar_Frequencia(request, num_matricula):
        aluno = Aluno.objects.get(numero_matricula=num_matricula)
        if aluno and request.method == 'POST':
            disciplina = request.POST.get('disciplina')
            data = request.POST.get('data')
            presenca = request.POST.get('presenca')
            falta = 0
            if presenca:
                falta += 1
            nova_frequencia = Frequencia(matricula_aluno=num_matricula, disciplina=disciplina, data=data, presenca=presenca, falta=falta)
            nova_frequencia.save()
            return redirect('home')
        else:
             return render(request, 'pages/cadastro_nota.html', {'aluno':aluno})

# class Turma:
#     def salvar_aluno_turma(request, aluno):
#         novo_aluno_turma = Turma(matricula_aluno=aluno.numero_matricula, porcentagem_aprovacao=None, media_frequencia=None, media_notas=None) #COLOCAR RETORNO DOS METODOS DE PORCENTAGEM E MEDIAS
#         novo_aluno_turma.save()

#     def buscar_turma(request, num_matricula):
#         aluno = Aluno.objects.get(numero_matricula=num_matricula)
#         if aluno:
#             turma_aluno = Turma.objects.get(numero_matricula=num_matricula)

class Relatorios:
    #PRESENCA
    def media_presenca_aluno(request, num_matricula):
        #TODO

     def media_presenca_turma(request, num_matricula):
        #TODO
        pass
     
     #NOTA
     def media_nota_aluno(request, num_matricula):
        #TODO
        pass
     
     def media_nota_turma(request, num_matricula):
        #TODO
        pass
     
     #APROVACAO
    def media_aprovacao_aluno(request, num_matricula):
        #TODO
        pass
     
    def media_aprovacao_turma(request, num_matricula):
        #TODO
        pass