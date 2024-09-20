# Jogo da Forca

# Desenvolva uma versão simples do jogo da forca, onde o usuário deve adivinhar uma palavra escolhida aleatoriamente.

def palavraAtual(palavra, letra):
    palavraFinal = []
    for i in range(len(palavra)):
        if letra == palavra[i]:
            palavraFinal.append(letra)
        else:
            palavraFinal.append('_ ')
    return palavraFinal


palavra = input('Digite uma palavra: ').upper()
dica = input('Escreva uma dica sobre a palavra: ')
novaPalavra = list(palavra)

print('Você tem 7 chances!!!')
print('Sua dica para a palavra é "{}"'.format(dica))
print('Sua palavra tem {} letras: {}'.format(len(palavra), '_ ' * len(palavra)))

for i in range(8, 1, -1):
    tentativa = input('Digite uma letra: ').upper()
    if tentativa in palavra:
        print('Você acertou: ')
        print('Palavra atual é {}'.format(palavraAtual(palavra, tentativa)))
    else:
        print('Você errou! Agora restam {}'.format(i - 2))