import json
from estudante import *

def save_estudante(bdEstudante, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(bdEstudante, f, ensure_ascii=False, indent=4)
        
def load_estudante(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            estudante_load = json.load(f)
            return [Estudante(e['nome'], e['idade'], e['nota'], e['media']) for e in estudante_load]
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        return []