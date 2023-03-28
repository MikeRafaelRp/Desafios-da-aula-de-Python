from random import shuffle
n1 = str(input('Digite o nome número 1: '))
n2 = str(input('Digite o nome número 2: '))
n3 = str(input('Digite o nome número 3: '))
n4 = str(input('Digite o nome número 4: '))
nomes = [n1,n2,n3,n4]
shuffle(nomes)
print('A ordem sorteada é: {}'.format(nomes))