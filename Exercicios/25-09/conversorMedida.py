distancia = float(input('Digite uma distância em metros: '))

km = distancia / 1000
hm = distancia / 100
dan = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000

print('A distância de {} corresponde a: '.format(distancia))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dan'.format(dan))
print('{:.0f}dm'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))
#:.0f ----- Define a quantidade de casas decimais em um float