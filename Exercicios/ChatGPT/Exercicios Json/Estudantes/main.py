from estudante import *
from saveLoad import *

bdEstudante = loadEstudante('estudantes.json')

while True: 
    print('1) Cadastrar\n2) Listar\n0) finalizar')
    opcao = int(input('Digite sua opção: '))
   
    if opcao ==0:
        saveEstudantes(bdEstudante, 'estudantes.json')
        break
    
    elif opcao == 1:
        estudante = Estudante(input('Digite o seu nome: '), input('Digite sua média: '))
        bdEstudante.append(estudante)
        
        estudante.cadastrarCurso()
        
    elif opcao == 2:
        for est in bdEstudante:
            est.showEstudante()