import numpy as np

n = int(input('Digite o primeiro parâmetro para matriz: '))
m = int(input('Digite o segundo parâmetro para a matriz: '))

matriz = np.full((n, m), None)
maior = 0
linha, coluna = 0, 0

for i in range(n):
    for j in range(m):
        matriz[i][j] = int(input(f'Digite um número para linha {i}, coluna {j}: '))
        # if matriz[i][j] > maior:    --> Direto no input
        #     maior = matriz[i][j]
        #     linha = i
        #     coluna = j

for i in range(n):
    for j in range(m):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha = i
            coluna = j

print(matriz)
print(f'Número maior é {maior}. Presente na linha {linha}, coluna {coluna}')