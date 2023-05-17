num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite mais um número inteiro: '))
if num1 > num2:
    print('O primeiro valor {} é o maior'.format(num1))
elif num1 < num2:
    print('O segundo valor {} é o maior'.format(num2))
else:
    print('Não existe maior, o primeiro valor {} e o segundo valor {} são iguais.'.format(num1,num2))
