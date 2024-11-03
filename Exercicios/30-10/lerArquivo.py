import re
import os

caminho = os.path.abspath('texto.txt')

with open(caminho, 'r', encoding='utf-8') as texto:
    texto = texto.read()
    
print(texto)
print(re.findall(r'\b[aeiouAEIOU]\w*', texto))