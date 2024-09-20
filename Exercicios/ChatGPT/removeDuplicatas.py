# Remover Duplicatas de uma Lista

# Escreva uma função que receba uma lista e retorne uma nova lista sem valores duplicados.

listaNumero = []
listaFinal = []

while True:
    try:
        listaNumero.append(int(input('Digite um número inteiro ou qualquer letra para finalizar a lista: ')))
    except ValueError:
        print('Finalizando a lista!')
        break

for i in range(len(listaNumero)):
    if listaNumero[i] not in listaFinal:
        listaFinal.append(listaNumero[i])

print('Lista Original: {}'.format(listaNumero))
print('Lista final: {}'.format(listaFinal))