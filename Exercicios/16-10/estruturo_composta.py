# https://www.youtube.com/watch?v=mlwt2CRQkTQ&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=6

import random

tupla = tuple(random.randint(1, 100) for _ in range(5))

num_maior = 0
num_menor = tupla[0]

for num in tupla:
    if num > num_maior:
        num_maior = num
    if num < num_menor:
        num_menor = num

print(tupla)
print(f'O maior valor sorteado foi: {num_maior}')
print(f'O menor número sorteado foi: {num_menor}')