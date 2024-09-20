n1 = int(input('Digite um número base para a taboada: '))

print('Para a taboada do {} temos: '.format(n1))
print('-' * 12)
for i in range(1, 11):
    # :2 ---------- Define 2 digitos para os números
    print('{} x {:2} = {}'.format(n1, i, n1 * i))

print('-' * 12)