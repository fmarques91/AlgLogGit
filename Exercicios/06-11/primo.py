def eh_primo(x):
    primo = 0
    if x == 1:
        return False
    else:
        for i in range(1, x + 1):
            if x % i == 0:
                primo += 1
        if primo == 2:
            return True
        else:
            return False

x = int(input())
if eh_primo(x):
    print('S')
else:
    print('N')