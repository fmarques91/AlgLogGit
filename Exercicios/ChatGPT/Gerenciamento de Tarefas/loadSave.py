from tarefa import Tarefa
import json

def salvar_tarefas(bdTarefas, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f: # Faz a gravação do arquivo, e adiciona encoding='utf-8'
        json.dump([tarefa.__dict__ for tarefa in bdTarefas], f, ensure_ascii=False) # Grava linha por linha com o "for" .Garante que os caracteres sejam gravados corretamente
        
        
# Função para carregar as tarefas de um arquivo JSON
def carregar_tarefas(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            tarefas_json = json.load(f) #Cria uma variável para armazenar a leitura do arquivo json, referenciado por "f"
            return [Tarefa(t['titulo'], t['descricao'], t['status']) for t in tarefas_json]  # Criando instâncias de Tarefa utilizando a variável "t" dentro do for
    except FileNotFoundError:
        return []  # Retorna lista vazia se o arquivo não existir
        