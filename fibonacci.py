#Exemplo Fibonacci: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610

final = int(input('Digite até quanto irá o calculo: '))

f = []

for i in range(final):
    if i <= 1:
        f.append(i)
    else:
        f.append(f[i - 1] + f[i - 2])

    if f[i] > final:
        f.pop()
        break

print(f)