from aluno import *
from saveLoad import *
from funcoes import *

bdAluno = loadAlunos('bdAluno.json')

while True:
    opcao = menu()
    
    if opcao == 1:
        aluno = Aluno(input('Nome: '), input('Idade: '), input('Nota: '))
        
        bdAluno.append(aluno)
    elif opcao == 2:
        for aluno in bdAluno:
            aluno.showAluno()
    elif opcao == 3:
        retorno = notaAcima(bdAluno)
        print('*' * 5, 'ALUNOS COM NOTAS ACIMA DE 7', '*' * 5)
        for aluno in retorno:
            aluno.showAluno()
    elif opcao == 0:
        saveAlunos(bdAluno, 'bdAluno.json')
        break