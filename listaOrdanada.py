#['30', '10', '30', '20', '15', '23', '18']


lista = []
listaFinal =[]

while True:
    numero = input('Digite um número ou Close, para sair: ')
    if numero.lower() == 'sair':
        break
    else:
        lista.append(numero)


for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[i] > lista[j]:
            