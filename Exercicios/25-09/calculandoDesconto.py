preco = float(input('Qual o preço do produto: R$'))

desconto = preco - preco * 0.05

#:.0f ----- Define a quantidade de casas decimais em um float
print('O produto que custa R${:.2f}, na promoção de 5% vai custar R${:.2f}'.format(preco, desconto))