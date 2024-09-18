palavra = input('Digite uma palavra: ')
palavra2 = input('Digite sua segunda palavra: ')

def transformaLista(p1):
    retorno = []
    for letra in p1:
        retorno.append(letra)
    return retorno

anagrama = 0
qtdPalavra = len(palavra)
palavra2 = transformaLista(palavra2)

if qtdPalavra != len(palavra2):
    print('Estas palavras não são anagramas!')
else:
    for i in range(qtdPalavra):
        for j in range(qtdPalavra):
            if palavra[i] == palavra2[j]:
                anagrama += 1
                palavra2[j] = ''
                break

    if anagrama == qtdPalavra:
        print('Estas palavras são anagramas!')
    else:
        print('Estas palavras não são anagramas!')