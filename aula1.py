nome = input('Qual o seu nome: ')
idade = input('Qual a sua idade: ')
peso = input('Qual o seu peso: ')

print('Seu nome é', nome + ', você tem', idade, 'anos de idade, e pesa', peso + 'kg')

op = 1
while op != 0:
    n1 = int(input('Digite o primeiro número da conta '))
    n2 = int(input('Digite o segundo número da sua conta: '))
    
    print('Sua soma é:', n1 + n2)
    
    op = int(input('Deseja fazer uma nova soma? Digite o número 1 para "SIM" e 0 para "NÃO": '))
    while True: 
        if op == 0 or op == 1:
            break
        else:
            op = int(input('Digite uma opção válida, 1 para "SIM" ou 0 para "NÃO": '))