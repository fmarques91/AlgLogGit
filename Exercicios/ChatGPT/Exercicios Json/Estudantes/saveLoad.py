from estudante import *
import json

def saveEstudantes(bdEstudante, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump([estudante.__dict__ for estudante in bdEstudante], f, ensure_ascii=False)
        
def loadEstudante(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            estudanteLoad = json.load(f)
            return [Estudante(est['nome'], est['media']) for est in estudanteLoad]
    except FileNotFoundError:
        return []