lista1 = [2, 4, 7, 4, 7, 8, 10, 5, 10]
lista2 = [5, 7, 3, 9, 10, 4, 8, 2]
listaFinal = []

for i in range(len(lista1)):
    for j in range(len(lista2)):
        if lista1[i] == lista2[j]:
            if lista1[i] not in listaFinal:
                listaFinal.append(lista1[i])

listaFinal.sort()                
print(listaFinal)