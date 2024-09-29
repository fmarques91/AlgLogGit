# Jogo de Adivinhação

# Crie um jogo onde o computador escolhe um número aleatório entre 1 e 100 e o usuário deve adivinhá-lo, 
# recebendo dicas de "maior" ou "menor".
def jogo(n1, n2):
    tentativas = 0
    if n1 == n2:
        print('Parabéns, você acertou de primeira!!!!!!')
    else:
        while n1 != n2:
            if isinstance(n1, int):
                if n2 > n1:
                    n1 = int(input('Você errou, o número sorteado é maior, digite um novo valor para tentar novamente ou 0 para finalizar o jogo: '))
                elif n2 < n1:
                    n1 = int(input('Você errou, o número sorteado é menor, digite um novo valor para tentar novamente ou 0 para finalizar o jogo: '))
                tentativas += 1
            else:
                print('Digite um número inteiro válido: ')

            if n1 == 0:
                print('Jogo finalizado!!!')
                break
                
            if n1 == n2:
                print('Parabéns, você acertou em {} tentativas!!!!!!'.format(tentativas))

import random

print('*' * 40 + '\nVamos começar o JOGO!!!!!!\n' + '*' * 40)

numeroInicial = int(input('Adivinhe o número de 1 a 100: '))
sort = random.randint(1, 100)

jogo(numeroInicial, sort)