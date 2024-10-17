# https://www.youtube.com/watch?v=1u7oA8ckjAc&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=8

tupla = ()
pares = ()

for _ in range(4):
    num = tuple(input('Digite um número: '))
    tupla += num

    
print(f'Você digitou os valores: {tupla}')
if '9' in tupla:
    print(f'Você digitou o número 9, {tupla.count('9')} vezes.')
else:
    print('Não existe 9 na tupla.')
if '3' in tupla:
    print(f'Você digitou o número 3 na {tupla.index('3')+1}ª posição.')
else:
    print('Não existe 3 na tupla.')
print('Estes são os números pares digitados: ', end='')
for numero in tupla:
    if int(numero) % 2 == 0:
        print(numero, end=' ')