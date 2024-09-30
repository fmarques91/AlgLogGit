while True:
    n = input('Digite um número para calcular seu fatorial: ')

    try:
        n = int(n)
        print('Número: ', n)
        break
    except ValueError:
        print('Digite uma opção válida!')

fatorial = 1
print('Calculando {}! = '.format(n), end='')
for i in range(n, 0, -1):
    print(str(i), 'x ' if i != 1 else '= ', end='')
    fatorial = fatorial * i
print(fatorial)