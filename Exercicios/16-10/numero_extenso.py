from num2words import num2words

numero = None
while numero != 0:
    numero = int(input('Digite um número: '))
    
    numero_extenso = num2words(numero, lang='pt_br').title()
    
    print(f'Você digitou o número {numero_extenso}')