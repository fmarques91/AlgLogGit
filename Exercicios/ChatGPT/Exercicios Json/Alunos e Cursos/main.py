from aluno import *
from saveLoad import *
from funcoes import *
from curso import *

bdAluno = loadAlunos('bdAluno.json')

while True:
    opcao = menu()
    
    if opcao == 1:
        aluno = Aluno(input('Nome: '), input('Idade: '))
        opcao = 0
        while opcao != 'sair':
            opcao = int(input('1) Cadastrar\n0) Sair: '))
            if opcao == 0:
                break
            curso = Curso(input('Curso: '), input('Nota: '))
            aluno.curso.append(curso)
        
        bdAluno.append(aluno)
    elif opcao == 2:
        for aluno in bdAluno:
            aluno.showAluno()
    elif opcao == 3:
        print
    elif opcao == 0:
        # saveAlunos(bdAluno, 'bdAluno.json')
        break