import numpy as np

estoque = {'caderno': 10,
           'caneta': 5,
           'lapis': 8,
           'borracha': 12,
           'lapiseira': 7,
           'corretivo': 15
           }

def showEstoque():
    print('=' * 20)
    for produto, valor in estoque.items():
        print(f'{produto}: {valor}')
    print('=' * 20)

while True:
    print('1) Adicionar Produtos')
    print('2) Atualizar Quantidade')
    print('3) Remover Produtos')
    print('4) Listar Produtos')
    print('0) Sair')
    opcao = int(input('Digite sua opção: '))
    
    if opcao == 1:
        produto = input('Digite o nome do produto: ').lower()
        estoque[produto] = int(input('Quantidade: '))
    elif opcao == 2:
        showEstoque()
        alterarProduto = input('Qual produto deseja alterar: ').lower()
        if alterarProduto in estoque:
            estoque[alterarProduto] = int(input('Digite o novo valor: '))
        else:
            print(alterarProduto, 'não encontrado no estoque.\n')
    elif opcao == 3:
        showEstoque()
        removerProduto = input('Qual produto deseja remover: ').lower()
        
        if removerProduto in estoque:
            estoque.pop(removerProduto)
            print('Produto removido!!!\n')
        else:
            print('Produto não encontrado.\n')
    elif opcao == 4:
        showEstoque()
    elif opcao == 0:
        precos = np.array([10.0, 3, 2.50, 0.50, 10.0, 4.70])
        qtd = np.array(list(estoque.values()))
        
        valorTotal = np.dot(precos, qtd)
        print(f'O estoque possui o valor total de R${valorTotal:.2f} reais')        
        break