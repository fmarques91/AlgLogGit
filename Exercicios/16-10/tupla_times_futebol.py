times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco',
         'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 
         'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

i = 0

print('Cinco primeiros colocados: ', end='')

# Outra forma de ser feito >>>>> print(times[0 : 5])
for i in range(0, 5):
    print(times[i], end='')
    
    if i < 4:
        print(', ', end='')

# Outra forma de ser feito >>>>> print('times[-4 : ]')
print('\nOs ultimos colocados são: ', end='')
for i in range(-1, -5, -1):
    print(times[i], end='')
    
    if i > -4:
        print(', ', end='')
        
print('\nOs times em ordem alfabética:', tuple(sorted(times)))

print('Chapecoense se encontra na posição:' ,times.index('Chapecoense') + 1)