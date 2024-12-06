import random

def palavraAtual(palavra, letra):
    
    for i in range(len(palavra)):
        if letra == palavra[i]:
            palavraFinal[i] = letra

    return palavraFinal

def desenhoForca(tentativa, palavra, letra):
    if tentativa == 7:
        print(' _________')
        print('|         |')
        print('|')
        print('|')
        print('|')
        print('|')
        print(f'|  {" ".join(palavraAtual(palavra, letra))}')
    elif tentativa == 6:
        print(' _________')
        print('|         |')
        print('|         O')
        print('|')
        print('|')
        print('|')
        print(f'| {" ".join(palavraAtual(palavra, letra))}')
    elif tentativa == 5:
        print(' _________')
        print('|         |')
        print('|         O')
        print('|         |')
        print('|')
        print('|')
        print(f'| {" ".join(palavraAtual(palavra, letra))}')
    elif tentativa == 4:
        print(' _________')
        print('|         |')
        print('|         O')
        print('|        /|')
        print('|')
        print('|')
        print(f'| {" ".join(palavraAtual(palavra, letra))}')
    elif tentativa == 3:
        print(' _________')
        print('|         |')
        print('|         O')
        print('|        /|\\')
        print('|')
        print('|')
        print(f'| {" ".join(palavraAtual(palavra, letra))}')
    elif tentativa == 2:
        print(' _________')
        print('|         |')
        print('|         O')
        print('|        /|\\')
        print('|        /')
        print('|')
        print(f'| {" ".join(palavraAtual(palavra, letra))}')
    elif tentativa == 1:
        print(' _________')
        print('|         |')
        print('|         O')
        print('|        /|\\')
        print('|        / \\')
        print('|')
        print(f'| {" ".join(palavraAtual(palavra, letra))}')

dicPalavra = [
    {"palavra": "Mamute", "dica": "Animal já instindo, viveu na era do gelo."},
    {"palavra": "Futebol", "dica": "Esporte jogado com os pés e um dos mais famosos pelo mundo."},
    {"palavra": "Aranha", "dica": "Animal conhecido por botar medo em muitas pessoas e ser pequeno, também deu origem a um super herói."},
    {"palavra": "Violão", "dica": "Instrumento famoso por ser porta de entrada para diversos instrumentos de corda."},
    {"palavra": "Chocolate", "dica": "Doce conhecido por ser vilão em muitas dietas."},
    {"palavra": "Avião", "dica": "Criado por um Brasileiro, e hoje usado por todo o mundo."}
]

sortPalavra = random.randint(0, len(dicPalavra) - 1)

palavra = dicPalavra[sortPalavra]['palavra'].upper()

palavraFinal = ['_'] * len(palavra)
letraRepetida = []

print('Você tem 7 chances!!!')
print('Sua dica para a palavra é "{}"'.format(dicPalavra[sortPalavra]['dica']))
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
            desenhoForca(i, palavra, tentativa)
            print('Você possui {} tentativas!'.format(i))
            print('*' * 100)
        else:
            if i == 1:
                i -= 1
                print('Que pena, você perdeu o jogo!!')
            else:
                i -= 1
                print('Você errou! Agora restam {} tentativas!'.format(i))
                desenhoForca(i, palavra, tentativa)
                letraRepetida.append(tentativa)
                print('E você já utilizou estas letras: {}'.format(letraRepetida))
                print('*' * 100)
    
    if list(palavra) == palavraFinal:
        print('*' * 100)
        print('PARABÉNS, VOCÊ GANHOU, ACERTOU A PALAVRA: {}'.format(palavra))
        print('*' * 100)
        break