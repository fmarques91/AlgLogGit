from tarefa import Tarefa, concluirTarefa, listarTarefas
import json

def salvar_tarefas(bdTarefas, arquivo):
    with open(arquivo, 'w', encoding='utf-8') as f: # Faz a gravação do arquivo, e adiciona encoding='utf-8'
        json.dump([{'titulo': tarefa.titulo, 'descricao': tarefa.descricao, 'status': tarefa.status} for tarefa in bdTarefas], f, ensure_ascii=False) # Grava linha por linha com o "for" .Garante que os caracteres sejam gravados corretamente
        
        
# Função para carregar as tarefas de um arquivo JSON
def carregar_tarefas(arquivo):
    try:
        with open(arquivo, 'r') as f:
            tarefas_json = json.load(f) #Cria uma variável para armazenar a leitura do arquivo json, referenciado por "f"
            return [Tarefa(t['titulo'], t['descricao'], t['status']) for t in tarefas_json]  # Criando instâncias de Tarefa utilizando a variável "t" dentro do for
    except FileNotFoundError:
        return []  # Retorna lista vazia se o arquivo não existir


bdTarefas = carregar_tarefas('tarefas.json')

while True:
    opcao = int(input('"OPÇÕES"\n1) Incluir uma nova tarefa. \n2) Marcar tarefa como concluida. \n3) Listar tarefas.\n4) Sair.\nDigite sua opção: '))

    if opcao == 1:
        tarefaInclusao = Tarefa(input('Digite o nome da sua tarefa: '), input('Digite a descrição da sua tarefa: '))
        bdTarefas.append(tarefaInclusao)
    elif opcao == 2:
        concluirTarefa(bdTarefas)
    elif opcao == 3:
        while True:
            print('-' * 5, 'OPÇÕES', '-' * 5)
            print('1) Filtrar por concluídos.\n2) Filtrar por pendentes.\n3) Listar todos\n4) Sair.')
            opcao2 = int(input('Digite sua opção: '))
            if opcao2 == 4:
                break
            else:
                listarTarefas(opcao2, bdTarefas)
    elif opcao == 4:
        salvar_tarefas(bdTarefas, 'tarefas.json')
        break
    else:
        print('\nDigite uma opção válida!\n')