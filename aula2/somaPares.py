n = int(input('Digite um valor: '))

soma = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        soma = soma + i

print('A soma dos número pares é: ', soma)