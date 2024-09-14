palavra = str(input('Digite uma palavra: '))
qtdPalavra = len(palavra)

contr = ''
igual = 0

for letra in range(qtdPalavra-1, -1, -1):
    contr += palavra[letra]

for letra in range(0, qtdPalavra):
    if contr[letra] != palavra[letra]:
        print(palavra, 'não é igual de trás para frente!')
        break
    else:
        igual += 1

if igual == len(palavra):
    print(palavra, 'é igual de trás para frente!')