# Gerador de Senhas

# Desenvolva um gerador de senhas aleatórias com uma determinada quantidade de caracteres, que pode incluir letras, números e símbolos.

import random
import string

senhaFinal = ''

print('Gerador de senhas\n', '*' * 100)

caracteres = '!@#$%¨&*;.,'

for i in range(5):
    senhaFinal += random.choice(caracteres)
    senhaFinal += random.choice(string.ascii_letters)
    senhaFinal += str(random.randint(0, 9))

print(' Sua senha final é: {}\n'.format(senhaFinal), '*' * 100)