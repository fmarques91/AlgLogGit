largura = float(input('Largura da Parede: '))
altura = float(input('Altura da Parede: '))

area = largura * altura
tinta = area / 2

print('Sua parede tem dimensão de {} x {} e sua área é de {}m².'.format(largura, altura, area))
print('Para pintar esta parede você irá utilizar {}l de tinta.'.format(tinta))