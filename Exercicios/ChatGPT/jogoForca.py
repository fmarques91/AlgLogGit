# Jogo da Forca

# Desenvolva uma versão simples do jogo da forca, onde o usuário deve adivinhar uma palavra escolhida aleatoriamente.

def palavraAtual(palavra, letra):
    
    for i in range(len(palavra)):
        if letra == palavra[i]:
            palavraFinal[i] = letra

    return palavraFinal

palavra = list(input('Digite uma palavra: ').upper())
dica = input('Escreva uma dica sobre a palavra: ')
palavraFinal = ['_'] * len(palavra)
letraRepetida = []

print('Você tem 7 chances!!!')
print('Sua dica para a palavra é "{}"'.format(dica))
print('Sua palavra tem {} letras: {}'.format(len(palavra), '_ ' * len(palavra)))

i = 7
while i >= 1:
    tentativa = input('Digite uma letra: ').upper()

    if tentativa in letraRepetida:
        print('Estas letras já foram utilizadas {}, tente outra!'.format(letraRepetida))
        print('*' * 100)
    else:    
        if tentativa in palavra:
            print('Você acertou a letra: ')
            letraRepetida.append(tentativa)
            print('Palavra atual é {} e você possui {} tentativas!'.format(palavraAtual(palavra, tentativa), i))
            print('*' * 100)
        else:
            if i == 1:
                i -= 1
                print('Que pena, você perdeu o jogo!!')
            else:
                i -= 1
                print('Você errou! Agora restam {} tentativas!'.format(i))
                letraRepetida.append(tentativa)
                print('E você já utilizou estas letras: {}'.format(letraRepetida))
                print('*' * 100)
    
    if palavra == palavraFinal:
        print('*' * 100)
        print('PARABÉNS, VOCÊ GANHOU, ACERTOU A PALAVRA: {}'.format(palavra))
        print('*' * 100)
        break