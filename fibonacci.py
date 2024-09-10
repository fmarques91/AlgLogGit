#Exemplo Fibonacci: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610

final = int(input('Digite até quanto irá o calculo: '))

f = 0
for i in range(1, final + 1):
    print(i + f)
    f = i