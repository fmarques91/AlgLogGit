palavra = input('Digite uma palavra: ')
qtdVolgal = 0


for letra in palavra:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        qtdVolgal += 1

print(palavra, 'possui', qtdVolgal, 'vogais!')