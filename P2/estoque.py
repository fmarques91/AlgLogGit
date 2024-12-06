import numpy as np

estoque = [
    {'produto':'arroz', 'quantidade':5, 'valor':5.50},
    {'produto':'feijão', 'quantidade':9, 'valor':8.70},
    {'produto':'farinha de trigo', 'quantidade':10, 'valor':4.70},
    {'produto':'óleo', 'quantidade':7, 'valor':8.00},
    {'produto':'sal', 'quantidade':10, 'valor':2.90}
]

def showEstoque():
    print('=' * 20)
    for produto in estoque:
        print(f'{produto['produto'].title()}: R${produto['valor']:.2f}')
        print(f'Qtd em estoque: {produto['quantidade']}')
        print('=' * 20)

while True:
    print('1) Adicionar Produtos')
    print('2) Remover Produtos')
    print('3) Verificar Quantidade')
    print('4) Listar Produtos')
    print('0) Sair')
    opcao = int(input('Digite sua opção: '))
    
    if opcao == 1:
        novoCadastro = {
            'produto' : input('Novo produto a ser cadastrado: ').lower(),
            'quantidade': int(input('Digite a quantidade em estoque: ')),
            'valor' : float(input('Digite o valor unitário do produto: '))
        }
        estoque.append(novoCadastro)

    elif opcao == 2:
        showEstoque()
        removerProduto = input('Qual produto deseja remover: ').lower()
        
        for i in range(len(estoque)):
            if estoque[i]['produto'] == removerProduto:
                estoque.pop(i)
                print('=' * 20)
                print(f'Produto "{removerProduto.title()}" removido com sucesso!!!\n')
                print('=' * 20)
                break
        else:
            print('=' * 20)
            print(f'Produto "{removerProduto}" não encontrado.\n')
            print('=' * 20)
            
    elif opcao == 3:
        verificarProduto = input('Qual produto deseja verificar: ').lower()
        
        for produto in estoque:
            if produto['produto'] == verificarProduto:
                print('=' * 20)
                print(f'O {verificarProduto} possui um total de {produto['quantidade']} unidades em estoque.')
                print('=' * 20)
                break
        else:
            print('=' * 20)
            print(f'{verificarProduto.title()} não foi encontrado em estoque.')
            print('=' * 20)
                
    elif opcao == 4:
        showEstoque()
    elif opcao == 0:
        precos = np.array([10.0, 3, 2.50, 0.50, 10.0, 4.70])
        qtd = np.array(list(estoque.values()))
        
        valorTotal = np.dot(precos, qtd)
        print(f'O estoque possui o valor total de R${valorTotal:.2f} reais')        
        break