while True:
    n = input('Digite um número para calcular seu fatorial: ')

    try:
        n = int(n)
        print('Número:', n)
        break
    except ValueError:
        print('Digite uma opção válida!')

fatorial = 1
print('Calculando {}! = '.format(n), end='')
while n > 0:
    print(str(n), 'x ' if n > 1 else '= ', end='')
    fatorial = fatorial * n
    n -= 1
print(fatorial)