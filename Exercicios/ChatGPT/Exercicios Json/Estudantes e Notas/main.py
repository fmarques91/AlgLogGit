from estudante import *
from saveLoad import *

bdEstudante = load_estudante('bdEstudante.json')

while True:
    print('*' * 5, 'OPÇÕES', '*' * 5)
    print('1) Cadastrar')
    print('2) Adicionar nova nota')
    print('3) Listar')
    print('4) Filtrar')
    print('0) Sair')
    opcao = int(input('Digite sua opção: '))
    
    if opcao == 1:
        estudante = Estudante(input('Digite o seu nome: '), input('Digite sua idade: '))
        estudante.cadastrar_nota()
        bdEstudante.append(estudante)
    elif opcao == 2:
        nome = input('Digite o nome do estudante que deseja adicionar notas: ')
        for est in bdEstudante:
            if est.nome.upper() == nome.upper():
                print(f'Encontrado as notas do estudante {est.nome}')
                print(f'Notas: {est.nota}')
                est.cadastrar_nota()
                break
        else:
            print(f'Estudante {nome} não encontrado!')
    elif opcao == 3:
        for est in bdEstudante:
            est.show_estudante()
    elif opcao == 4:
        media = float(input('Digite a média que deseja buscar: '))
        media_acima = filtrar_estudante(bdEstudante, media)
        for m in media_acima:
            m.show_estudante()
    elif opcao == 0:
        dict_bdEstudante = [e.to_dict() for e in bdEstudante]
        save_estudante(dict_bdEstudante, 'bdEstudante.json')
        break
    else:
        print('Digite uma opção válida!')