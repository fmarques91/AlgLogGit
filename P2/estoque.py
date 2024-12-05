import numpy as np

estoque = [
    {'produto':'Arroz', 'quantidade':5, 'valor':5.50},
    {'produto':'Feijão', 'quantidade':9, 'valor':8.70},
    {'produto':'Farinha de Trigo', 'quantidade':10, 'valor':4.70},
    {'produto':'Óleo', 'quantidade':7, 'valor':8.00},
    {'produto':'Sal', 'quantidade':10, 'valor':2.90}
]

def showEstoque():
    print('=' * 20)
    for i in range(len(estoque)):
        for produto, quantidade, valor in estoque.items():
            print(f'{produto}: {valor}')
            print(f'Quantidade em estoque: {quantidade}')
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