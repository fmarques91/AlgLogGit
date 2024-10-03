import json
from aluno import Aluno
from curso import Curso

def dict_curso(cursos):
    return  [Curso(c['Curso'], c['nota']) for c in cursos] # Retorna uma lista com os objetos Curso

def saveAlunos(bdAlunos, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(bdAlunos, f, ensure_ascii=False, indent=4)
        
def loadAlunos(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f: # Abre o arquivo em formato de leitura e aceita carcacteres especiais
            bdAlunos_json = json.load(f)  # Salva o arquivo json em uma variável
            alunos = [Aluno(a['nome'], a['idade'], dict_curso(a['curso'])) for a in bdAlunos_json] # Adiciona os arquivos em um objeto Aluno
            
            return alunos
    except FileNotFoundError:
        print('Arquivo não encontrado!')
        return []