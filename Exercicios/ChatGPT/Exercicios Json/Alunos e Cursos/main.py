from aluno import *
from saveLoad import *
from curso import *

bdAluno = loadAlunos('bdAluno.json')

while True:
    print('*' * 5, 'OPÇÕES', '*' * 5)
    print('1) Cadastrar')
    print('2) Listar todos')
    print('0) Sair')
    
    opcao = int(input('Digite sua opção: '))
    
    if opcao == 1:
        aluno = Aluno(input('Nome: '), input('Idade: '))
        aluno.addCurso()
        
        bdAluno.append(aluno)
    elif opcao == 2:
        for aluno in bdAluno:
            aluno.showAluno()
            print('-=' * 20)
    elif opcao == 0:
        dict_bdAluno = [c.to_dict() for c in bdAluno]
        saveAlunos(dict_bdAluno, 'bdAluno.json')
        break
    else:
        print('Digite uma opção válida!!')