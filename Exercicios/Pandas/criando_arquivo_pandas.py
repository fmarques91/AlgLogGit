import pandas as pd

# dataframe = pd.DataFrame() # Cria um DataFrame
venda = {
    'data': ['15/02/2021', '16/02/2021'],
    'valor': [500, 300],
    'produto': ['feijao', 'arroz'],
    'qtde': [50,70]
}

vendas_df = pd.DataFrame(venda) #Cria um DataFrame com os dados no Panda

print(vendas_df)