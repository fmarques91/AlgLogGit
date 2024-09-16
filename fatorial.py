while True:
    n = input('Digite um número inteiro: ')

    try:
        n = int(n)

        print('Entrada válida!')
        break

    except ValueError:
        print('Digite um número válido!')

fatorial = 1
for i in range(n, 0, -1):
    print(fatorial, 'x', i)
    fatorial = fatorial * i

print(fatorial)