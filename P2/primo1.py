def primo(x):
    verificaPrimo = 0
    if x == 1:
        return False
    else:
        for i in range(1, x + 1):
            if x % i == 0:
                verificaPrimo += 1
        if verificaPrimo == 2:
            return True
        else:
            return False

x = 1
while x >= 0:
    x = int(input("Digite um número para verificarmos se ele é primo: "))
    if primo(x):
        print(f'{x} é um número primo!')
    else:
        print(f'{x} não é um número primo!')