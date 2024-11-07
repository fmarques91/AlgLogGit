lista = [4,3,7,9,5, 11, 4, 12]
 
for i in range(len(lista)):
  for j in range(i + 1, len(lista)):
    if lista[i] > lista[j]:
      print(lista[i], lista[j])
      print(lista)
      lista[i], lista[j] = lista[j], lista[i]
      print(lista)
 
print(lista)