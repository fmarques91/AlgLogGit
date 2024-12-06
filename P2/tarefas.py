tarefas = [{"titulo": "Levantamento", "descricao": "Levamento de requisitos para construção do Projeto", "prazo" : 8, "status": "Concluído"}, 
           {"titulo": "Protóripo", "descricao": "Criação de protótipo para apresentação ao cliente", "prazo" : 5, "status": "Concluído"}, 
           {"titulo": "Validação", "descricao": "Validação do protótipo com o cliente", "prazo" : 10, "status": "Concluído"}, 
           {"titulo": "Escopo desenvolvimento", "descricao": "Realizar o escopo para desenvolvimento, criação de diagramas e algorítmos", "prazo" : 11, "status": "Concluído"}, 
           {"titulo": "Desenvolvimento", "descricao": "Realizar o desenvolvimento do código em Python", "prazo" : 5, "status": "Pendente"}]

opcao = None
while opcao != 0:
    print('Gerenciador de Tarefas')
    print('1) Adicionar uma nova Tarefa.')
    print('2) Concluir Tarefa.')
    print('3) Filtrar Tarefa.')
    print('4) Editar Tarefas.')
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
            print