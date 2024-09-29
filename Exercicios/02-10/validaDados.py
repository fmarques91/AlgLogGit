sexo = input('Informe seu Sexo [M/F]: ').upper()

while sexo != 'M' and sexo != 'F':
    sexo = input('Dados inválidos. Por favor, informe se sexo: ').upper()

if sexo == 'M' or sexo == 'F':
    print('Sexo {} registrado com sucesso!'.format(sexo))