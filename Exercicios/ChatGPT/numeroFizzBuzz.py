numero = int(input('Digite um numero inteiro: '))
lista = []

for i in range(1, numero + 1):
    if i % 3 == 0 and i % 5 == 0:
        lista.append(str(i) + ' - FizzBuzz')
    elif i % 3 == 0:
        lista.append(str(i) + ' - Fizz')
    elif i % 5 == 0:
        lista.append(str(i) + ' - Buzz')
    else:
        lista.append(str(i))

for item in lista:
    print(item)