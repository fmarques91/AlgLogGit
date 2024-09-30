print('Gerador de PA')
print('-=' * 10)
primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))

i = 0
while i < 10:
    print(primeiroTermo, '-> ', end='')
    primeiroTermo += razao
    i += 1
print('Fim!')