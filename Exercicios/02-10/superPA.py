print('Gerador de PA')
print('-=' * 10)
primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))

i = 0
num = 10
termo = 0
while i < num:
    print(primeiroTermo, '-> ', end='')
    primeiroTermo += razao
    i += 1
    
    
    if i == num:
        print('Pausa')
        termo += num
        num = int(input('Quantos termos você quer mostrar a mais? '))
        if num == 0:
            break
        i = 0
        
print('Progressão finalizada com {} termos mostrados.'.format(termo))