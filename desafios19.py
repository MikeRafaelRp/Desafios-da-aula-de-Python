from random import choice
aluno1 = str(input('Digite o nome do aluno número 1: '))
aluno2 = str(input('Digite o nome do aluno número 2: '))
aluno3 = str(input('Digite o nome do aluno número 3: '))
aluno4 = str(input('Digite o nome do aluno número 4: '))
alunos = [aluno1,aluno2,aluno3,aluno4]
sorteio = choice(alunos)
print('O aluno sorteado foi: {}'.format(sorteio))