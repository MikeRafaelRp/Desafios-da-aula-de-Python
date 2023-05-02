casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Quanto anos você vai pagar? '))
minimo = salario * 30 / 100
prestacao = casa / (anos * 12)
if prestacao <= minimo:
    print('A prestação mensal fica em: {:.2f}$'.format(prestacao))
else:
    print('Empréstimo negado!{:.2f}'.format(prestacao))