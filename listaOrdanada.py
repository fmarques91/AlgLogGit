#['30', '10', '30', '20', '15', '23', '18']


lista = []

while True:
    numero = input('Digite um número ou Close, para sair: ')
    if numero.lower() == 'sair':
        break
    else:
        lista.append(numero)

lista.sort()

print(lista)