import numpy as np

matriz = np.array([[None, None, None],
                   [None, None, None],
                   [None, None, None]
                  ])

velha = True

def show_jogo():
  print('*' * 10)
  print(matriz[0])
  print(matriz[1])
  print(matriz[2])
  print('*' * 10)

def acao(jogador):
    print(f'Jogador {jogador}')
    linha = int(input('Em qual linha deseja jogar? '))
    coluna = int(input('Em qual coluna deseja jogar? '))
    try:
        if matriz[linha - 1][coluna - 1] != None:
            print('Esta posição já foi jogada, escolha outra.')
            show_jogo()
            acao(jogador)
        else:
            matriz[linha - 1][coluna - 1] = jogador
            show_jogo()
    except IndexError:
        print('Digite uma opção válida.')
        acao(jogador)
    
def ganhador(jogador):
    diag = 0
    diag2 = 0
    for i in range(3):
        if matriz[i][i] == jogador:
            diag += 1
        if matriz[i][2 - i] == jogador:
            diag2 += 1
        horizontal = 0
        vertical = 0
        for j in range(3):
            if matriz[i][j] == jogador:
                horizontal += 1
            if matriz[j][i] == jogador:
                vertical += 1
                if horizontal == 3 or diag == 3 or diag2 == 3 or vertical == 3:
                    print(f'GANHADOR FOI O JOGADOR "{jogador}"')
                    return True

jogador1 = 'X'
jogador2 = 'O'
jogadas = 0
while None in matriz:

  (acao(jogador1))
  if ganhador(jogador1) == True:
      velha = False
      break
  
  if None in matriz:
    (acao(jogador2))
    if ganhador(jogador2) == True:
        velha = False
        break

if velha == True:
    print('Deu Velha!!!!')