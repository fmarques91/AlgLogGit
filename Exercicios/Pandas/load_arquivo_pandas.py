#Vídeo: https://www.youtube.com/watch?v=C0aj3FjN5e0

#DataFrames são tabelas importadas para o Python pelo Pandas
#"Pandas.Series" não são DataFrames mas sim uma unica coluna deles

import pandas as pd # Necessário a instalção (pip install pandas) para verificar versão (pip show pandas)

vendas_df = pd.read_excel('Vendas.xlsx') # Necessário instalação (pip install openpyxl) e para verificação (pip show openpyxl)

# print(vendas_df) # Imprime toda a planilha no terminal

# print(vendas_df.head(10)) # Parenteses vazio apresenta as 5 primeiras linhas, ou adicione a quantidade que deseja ver
# print(vendas_df.shape) # Apresenta quantas linhas e quantas colunas sua tabela possui
# print(vendas_df.describe()) # Faz basicamente uma análise detalhada sobre os dados da planilha

# produtos = vendas_df[['Produto', 'ID Loja']] # Pega somente as coluna listadas nos colchetes, para pegar somente uma, é necessário apenas um par de colchetes

# print(produtos)

# print(vendas_df.loc[1 : 5])  # Pega linhas específicas

# vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping']   # Pegar linhas que conrrepondem a uma condição
# print(vendas_norteshopping_df)

# vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']]   # Pegar dados que conrresponde a linhas e colunas impostas na função. Primeiro atributo linha, segundo coluna
# print(vendas_norteshopping_df)# Pegar várias linhas e colunas usando o loc

# print(vendas_df.loc[1, 'Produto'])# Pegar um valor especifico

vendas_df['Comissão'] = vendas_df['Valor Final'] * 0.05 # Adicionar nova coluna a partir de uma coluna que existe
# print(vendas_df)

vendas_df.loc[:, 'Imposto'] = 0  # Criar uma coluna com um valor padrão. ":" >>>> significa todas as linhas
# print(vendas_df)

vendas_dez_df = pd.read_excel('Vendas - Dez.xlsx')  # Adicionar 1 linha
vendas_df = pd.concat([vendas_df, vendas_dez_df]) # Concatena as duas planilhas
# print(vendas_df)

vendas_df = vendas_df.drop('Imposto', axis=1)   # Excluir colunas, axis(eixo), 1 é o eixo da coluna, 0 eixo da linha. Se não passar o eixo, por padrão exclui a linha
vendas_df = vendas_df.drop(0, axis=0)  # Exclui a linha 0 da planilha

vendas_df = vendas_df.dropna(how='all')   # Deletar linhas vazias, "All" >>>> exclui linhas ou colunas completamente vazias, se quiser excluir colunas passar o axis=1
print(vendas_df)