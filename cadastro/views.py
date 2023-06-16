from django.shortcuts import render, redirect, get_object_or_404
from . models import Aluno, Nota, Turma, Frequencia
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
from django.http import HttpResponse
import random

class ViewAluno:
    @login_required(redirect_field_name='login')
    def ver_aluno_turma(request):
        print(request.GET.get('cod_turma'))
        turma = Turma.objects.get(codigo_turma=request.GET.get('cod_turma'))
        turmas= Turma.objects.all()
        alunos = Aluno.objects.filter(turma_id=turma.codigo_turma)
        return render(request, 'pages/controle.html', {'alunos':alunos, 'turmas':turmas}) 



    @login_required(redirect_field_name='login')
    def ver_todos_alunos(request):
        turmas = Turma.objects.all()
        alunos = Aluno.objects.all()
        
        return render(request, 'pages/controle.html', {'alunos':alunos, 'turmas':turmas}) 

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
        return redirect( 'home')

    def adicionar_aluno(request):
        if request.method == 'POST':
            numero_matricula = Utils.gerar_num_matricula()
            nome = request.POST.get('nome')
            imagem = request.FILES.get('imagem')
            cpf = Validacao.mensagem_erro(request.POST.get('cpf'))
            email = request.POST.get('email')
            telefone = request.POST.get('telefone')
            telefone_emergencia = request.POST.get('telefone_emergencia')
            historico_familiar = request.POST.get('historico_familiar')
            data_nascimento = request.POST.get('data_nascimento')
            turma = request.POST.get('turma')

            turma_bd = Turma.objects.get(codigo_turma=turma)
                
            novo_aluno = Aluno(turma=turma_bd, numero_matricula=numero_matricula, nome=nome,cpf=cpf, email=email, historico_familiar=historico_familiar, data_nascimento=data_nascimento, telefone=telefone, telefone_emergencia=telefone_emergencia, imagem=imagem, aprovado=True)
            novo_aluno.save()

            return redirect( 'home')
        else:
            turmas = Turma.objects.all()
            return render(request, 'pages/cadastro_alunos.html', {'turmas':turmas})


    def editar_aluno(request, numero_matricula):
        if request.method == 'POST':
            aluno = Aluno.objects.get(numero_matricula=numero_matricula)
            numero_matricula = Utils.gerar_num_matricula()
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
            return redirect( 'home')
        else:    
            aluno = Aluno.objects.get(numero_matricula=numero_matricula)
            return render(request, 'pages/cadastro_alunos.html', {'aluno':aluno})

class ViewNota:
    def cadastrar_nota(request, numero_matricula):
        aluno = Aluno.objects.get(numero_matricula=numero_matricula)
        notas_aluno = Nota.objects.filter(matricula_aluno=aluno)
        if request.method == 'POST':
                disciplina = request.POST.get('disciplina')
                nota_1 = request.POST.get('nota_1')
                nota_2 = request.POST.get('nota_2')
                nota_3 = request.POST.get('nota_3')
                nota_4 = request.POST.get('nota_4')
                nota_final = request.POST.get('nota_final')
                aprovado = request.POST.get('aprovado')

                nova_nota = Nota(matricula_aluno=aluno, peso=1, disciplina="teste", nota_1=nota_1, nota_2=nota_2, nota_3=nota_3, nota_4=nota_4, nota_final=nota_final)
                nova_nota.save()
                # aluno.aprovado = aprovado
                # aluno.save()
                return redirect( 'home')
        if notas_aluno.exists():
            notas = Nota.objects.filter(matricula_aluno=aluno)
            return render(request, 'pages/cadastro_nota.html', {'aluno':aluno, 'notas':notas})
        else:
            return render(request, 'pages/cadastro_nota.html', {'aluno':aluno})

class ViewFrequencia:
    def cadastrar_frequencia(request, numero_matricula):
        aluno = Aluno.objects.get(numero_matricula=numero_matricula)
        frequencia_aluno = Frequencia.objects.filter(matricula_aluno=aluno)
        if request.method == 'POST':
                disciplina = 'WEB'
                checkado = request.POST.get('grupo')
                print(checkado)

                presenca = 0
                falta = False
                data = checkado
                if checkado:
                    presenca += 1
                    falta = True


                nova_frequencia = Frequencia(matricula_aluno=aluno, disciplina=disciplina, data=data, presenca=presenca, falta=falta)
                nova_frequencia.save()
                return redirect( 'home')
        if frequencia_aluno.exists():
            frequencias = Frequencia.objects.filter(matricula_aluno=aluno)
            for frequencia in frequencias:
                print(frequencia.data)

            return render(request, 'pages/cadastro_frequencia.html', {'aluno':aluno, 'frequencias':frequencias})
        else:
            print('n existe')
            return render(request, 'pages/cadastro_frequencia.html', {'aluno':aluno})
  


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

class Validacao:
    def mensagem_erro(campo):
        mensagem = {'ERRO': f'ERRO AO SALVAR {campo}"'}
        mensagem_json = json.dumps(mensagem)
        response = HttpResponse(mensagem_json, content_type='application/json')
        return response



    def validate_cpf(cpf):
        erro = False
        cpf_f = ''.join(filter(str.isdigit, cpf))

        if len(cpf_f) != 11:
            erro = True

        if cpf_f == cpf_f[0] * 11:
            erro = True
        
        if erro:
            Validacao.mensagem_erro("cpf")
        return cpf
    

class Utils:
    def gerar_num_matricula():
        num_matricula = random.randint(100000, 999999)
        return num_matricula