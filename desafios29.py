velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Você passou o limite, será multado em: {}'.format((velocidade - 80) * 7))
