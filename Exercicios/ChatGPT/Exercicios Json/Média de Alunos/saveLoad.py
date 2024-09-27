import json
from aluno import Aluno

def saveAlunos(bdAlunos, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump([aluno.__dict__ for aluno in bdAlunos], f, ensure_ascii=False)
        
def loadAlunos(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            bdAlunos_json = json.load(f)
            return [Aluno(a['nome'], a['idade'], a['nota']) for a in bdAlunos_json]
    except FileNotFoundError:
        return []