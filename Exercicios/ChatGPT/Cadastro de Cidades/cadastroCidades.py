import json

def cadastrarCidade():
    while True:
        print('*' * 5, 'OPÇÕES', '*' * 5)
        print('1 - Sair')
        variavel = input('Digite a Cidade / Estado: ')
        
        if variavel == '1':
            break
        elif variavel.isdigit():
            print('Digite uma opção válida!!!')
        else:
            cidades.append(variavel)

def removerCidade():
    while True:
        print('*' * 5, 'OPÇÕES', '*' * 5)
        print('1 - Para listar\n2 - Sair')
        variavel = input('Digite a cidade para remoção: ').upper()
        cidadesUp = [v.upper() for v in cidades]
        
        if variavel == '1':
            listarCidade()
        elif variavel == '2':
            break
        elif variavel.isdigit():
            print('Digite uma opção válida!!')
        elif variavel in cidadesUp:
            index = cidadesUp.index(variavel) #nome_variavel.index(valor_de referência) -> Retorna o indice do objeto dentro de uma lista
            removed = cidades.pop(index)   # pop() ->>>>> Remove algum indice de uma lista
            print('Cidade {} removida com sucesso! '.format(removed))
        else:
            print('Cidade {} não encontrada!'.format(variavel))  

def listarCidade():
    print('Cidades/Estados atuais: {}'.format(cidades))
    
def salvarCidades(cidades, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(cidades, f, ensure_ascii=False)
        
def lerCidades(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

cidades = lerCidades('cadastroCidades.json')

while True:
    print('*' * 5, 'OPÇÕES', '*' * 5)
    print('1) Cadastro de Cidades\n2) Listar Cidades\n3) Remover cidade\n4) Sair')
    opcaoInicial = input('Digite sua opção: ')
    
    try:
        opcao = int(opcaoInicial)
        if opcao == 1:
            cadastrarCidade()
        elif opcao == 3:
            removerCidade()
        elif opcao == 2:
            listarCidade()
        elif opcao == 4:
            salvarCidades(cidades, 'cadastroCidades.json')
            break
        else:
            print('Digite uma opcao válida!!!!')
    except ValueError:
        print('Digite uma opção válida!!!')