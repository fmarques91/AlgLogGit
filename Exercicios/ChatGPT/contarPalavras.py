# Contar Palavras em um Texto

# Crie um programa que conte o número de palavras em um texto fornecido pelo usuário.

frase = input('Digite uma frase: ')
listaFrase = []
palavra = ''

for letra in frase + ' ':
    if letra == ' ':
        listaFrase.append(palavra)
        palavra = ''
    else:
        palavra += letra

print('Esta frase contém {} palavras!'.format(len(listaFrase)))