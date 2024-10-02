from estudante import *
import json

def saveEstudantes(bdEstudante, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump([estudante.__dict__ for estudante in bdEstudante], f, ensure_ascii=False, indent=4)
        
def loadEstudante(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            estudanteLoad = json.load(f)
            estudantes = []
            for est in estudanteLoad:
                aluno =  Estudante(est['nome'], est['media'])
                aluno.curso = est['curso']
                estudantes.append(aluno)
            return estudantes
    except FileNotFoundError:
        return []