'''
Uma pista de Kart permite 10 voltas para cada um de 6 corredores. 
Faça um programa que leia os nomes e os tempos (em segundos) de cada volta de cada corredor e guarde as informações em uma matriz. 
Ao final, o programa deve informar:
a. De quem foi a melhor volta da prova, e em que volta
b. Classificação final em ordem (1º. o campeão)
c. Qual foi a volta com a média mais rápida
'''
import numpy as np

# Retorna o melhor tempo, volta e nome do piloto
def menorTempo(matriz):
    melhorTempo = float('inf')
    melhorVolta = None
    pilotoMelhorVolta = None
    for i in range(1, pilotos):
        for j in range(1, voltas):
            if matriz[i][j] <= melhorTempo:
                melhorTempo = matriz[i][j]
                pilotoMelhorVolta = matriz[i][0]
                melhorVolta = matriz[0][j]
    return pilotoMelhorVolta, melhorTempo, melhorVolta

def classificacao(matriz):
    dicPiloto = {}
    for i in range(1, pilotos):
        piloto = matriz[i][0] #Recebendo o nome do piloto para utilizar como chave de um dicionário
        dicPiloto[piloto] = np.sum(matriz[i][1:]) #Somando todas as voltas de um piloto
    classFinal = dict(sorted(dicPiloto.items(), key=lambda item: item[1])) #Função lambda, cria uma função simples e anônimas
    i = 1
    for chave, valor in classFinal.items():
        print(f'{i}º Colocado: {chave}, tempo: {valor} segundos.')
        i += 1


def MediaVoltaMaisRapida(matriz):
    valorFinal = float('inf')
    somaValor = 0
    for i in range(1, voltas):
        for j in range(1, pilotos):
            somaValor += matriz[j][i]
        somaValor = somaValor / (pilotos - 1)
        if somaValor < valorFinal:
            valorFinal = somaValor
            numeroVolta = matriz[0][i]
    return valorFinal, numeroVolta

#Define a quantidade de pilotos e voltas, necessário somar 1 linha e coluna a mais para o cabeçalho
pilotos, voltas = 7, 11

# Cria matriz com todos os valores em None
tempo = np.full((pilotos, voltas), None)

# Define o meu cabeçalho
tempo[0][0] = 'PILOTO'
for i in range(1, voltas):
    tempo[0][i] = f'{i}ª VOLTA'

# Define os nomes dos pilotos
espaco = 0
for i in range(1, pilotos):
    tempo[i][0] = input(f'Digite o nome do {i}° piloto: ')
    esp = len(tempo[i][0])
    if esp > espaco: #Recebe a quantidade de letras para utilizar no espaçamento da matriz
        espaco = esp

# Insere o tempo de cada volta dos pilotos
for j in range(1, voltas):
    for i in range(1, pilotos):
        tempo[i][j] = float(input(f'Digite o tempo da {j}ª volta do Piloto {tempo[i][0]}: '))

print('-=' * 30)
for linha in tempo:
    print(' '.join(f'{elemento:^{str(espaco)}}' for elemento in linha)) #Imprime a matriz formatada com o mesmo espaçamento entre as colunas
print('-=' * 30)
pilotoMelhorVolta, melhorTempo, melhorVolta = menorTempo(tempo)
print(f'O Piloto {pilotoMelhorVolta} teve o melhor tempo de {melhorTempo} segundos na {melhorVolta}')
print('-=' * 30)
classificacao(tempo)
print('-=' * 30)
mediaVolta, numeroVolta = MediaVoltaMaisRapida(tempo)
print(f'A {numeroVolta} teve a média mais rápida, com {mediaVolta:.2} segundos.')