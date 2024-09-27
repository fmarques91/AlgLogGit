def menu():
    print('*' * 5, 'OPÇÕES', '*' * 5)
    print('1) Cadastrar')
    print('2) Listar todos')
    print('3) Listar Alunos com notas maiores que 7')
    print('0) Sair')
    
    return int(input('Digite sua opção: '))

def notaAcima(lista):
    notasMaiores = []
    
    for aluno in lista:
        if int(aluno.nota) > 7:
          notasMaiores.append(aluno)
    return notasMaiores  