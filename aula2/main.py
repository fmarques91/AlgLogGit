from funcao import calc

n1 = int(input('Digite o primeiro número para sua operação: '))
n2 = int(input('Digite o segundo número para sua operação: '))
oper = str(input('Digite a operação desejada: '))

while oper != '*' and oper != '/' and oper != '-' and oper != '+':
    oper = str(input('Digite uma opção válida *, /, - ou +: '))

print('Resultado da sua operação,', n1, oper, n2, ', é: ', calc(n1, n2, oper))