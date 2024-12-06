import numpy as np

matriz1 = np.full((3, 3), 0)

matriz2 = np.random.randint(1, 100, size=(4, 4))
maior = 0
linha, coluna = 0, 0
somaLinha, somaColuna = 0, 0

for i in range(4):
    for j in range(4):
        if i == 3:
            somaLinha += matriz2[i][j]
        if j == 2:
            somaColuna += matriz2[i][j]
        if matriz2[i][j] > maior:
            maior = matriz2[i][j]
            linha = i
            coluna = j

print(matriz1)
print('=-' * 10)
print(matriz2)
print('=-' * 10)
print(f'Maior número da matrix 4x4 é {maior}, localizado na linha {linha}, coluna {coluna}')
print(f'A média da linha 3 é {somaLinha / 4}, e a média da coluna 2 é {somaColuna / 4}')