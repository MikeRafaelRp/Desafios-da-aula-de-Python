money = float(input('Digite o salário de um funcionário: '))
if money > 1250:
    novo = money * 10 / 100
    print('Aumento foi de: {}'.format(novo))
else:
    novo = money * 15 / 100
    print('Aumento foi de: {}'.format(novo))