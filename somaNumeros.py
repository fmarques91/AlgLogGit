palavra = input('Digite algo: ')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print('A soma entre {} + {} = {}'.format(n1, n2, (n1+n2)))

print('{} é do formato: {}'.format(palavra, type(palavra)))
print('{} é número? {}'.format(palavra, palavra.isnumeric()))
print('{} é alfanumérico? {}'.format(palavra, palavra.isalpha()))
print('{} é um espaço? {}'.format(palavra, palavra.isspace()))