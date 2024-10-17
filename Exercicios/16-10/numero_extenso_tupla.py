extenso = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 
           'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')


numero = None
while numero != 0:
    numero = int(input('Digite um número entre 0 e 20: '))
    
    if 0 <= numero <= 20:
        print(f'Número digitado é {extenso[numero]}')
    else:
        print('Digite um número válido!')