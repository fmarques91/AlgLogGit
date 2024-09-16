# Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se da mesma forma de trás para frente).

# Requisitos:

# A função deve ignorar espaços e diferenciar maiúsculas de minúsculas.
# O usuário deve fornecer a palavra ou frase.
# O programa deve informar se a entrada é ou não um palíndromo.

palavra = str(input('Digite uma palavra: '))
qtdLetras = len(palavra)

contrario = ''

for i in range(qtdLetras - 1, -1, -1):
        contrario += palavra[i]

if palavra == contrario:
        print(palavra, 'é Palíndromo!')
else:
        print(palavra, 'não é Palíndormo!')

