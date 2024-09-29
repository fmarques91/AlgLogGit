def num ():
    valor1 = int(input('Primeiro Valor: '))
    valor2 = int(input('Segundo Valor: '))

    return valor1, valor2
    
opcao = 0

valor1, valor2 = num()
while opcao != 5:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos Números')
    print('[ 5 ] Sair do Programa')
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        print('A soma de {} + {} é igual a {}'.format(valor1, valor2, valor1 + valor2))
    elif opcao == 2:
        print('A multiplicação de {} * {} é igual a {}'.format(valor1, valor2, valor1 * valor2))
    elif opcao == 3:
        print('O maior número entre {} e {} é: {}'.format(valor1, valor2, valor1 if valor1 > valor2 else valor2))
    elif opcao == 4:
        valor1, valor2 = num()
    elif opcao == 5:
        print('Finalizando a Aplicação!!!')
    else: 
        print('Digite uma opção válida! ')