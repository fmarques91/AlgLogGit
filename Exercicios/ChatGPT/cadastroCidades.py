cidades = []

def cadastrarCidade():
    while True:
        variavel = input('Digite a cidade/estado para cadastro, "s" para sair ou "l" para listar todas: ').upper()
        if variavel.isalpha():
            if variavel == 'S':
                break
            elif variavel == 'L':
                listarCidade()
            else:
                cidades.append(variavel)
        else:
            print('Digite uma opção válida!!!')

def removerCidade():
    while True:
        variavel = input('Digite a cidade/Estado para remover, "s" para sair ou "l" para listar todas: ').upper()
        if variavel.isalpha():
            if variavel == 'S':
                break
            elif variavel == 'L':
                listarCidade()
            else:
                if variavel in cidades:
                    cidades.remove(variavel)
                    print('Cidade {} removida com sucesso! '.format(variavel))
                else:
                    print('Cidade {} não encontrada!'.format(variavel))  
        else:
            print('Digite uma opção Válida!')

def listarCidade():
    print('Cidades/Estados atuais: {}'.format(cidades))


while True:
    opcaoInicial = input('Digite 1 para cadastrar cidades, ou 0 para remover, ou 2 para listar todas: ')
    
    try:
        opcao = int(opcaoInicial)
        if opcao == 1:
            cadastrarCidade()
        elif opcao == 0:
            removerCidade()
        elif opcao == 2:
            listarCidade()
        else:
            print('Digite uma opcao válida!!!!')
    except ValueError:
        print('Digite uma opção válida!!!')