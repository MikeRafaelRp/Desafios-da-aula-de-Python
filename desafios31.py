dist = int(input('Qual a distancia da viagem em Km? '))
if dist <= 200:
    print('O valor da sua passagem será: ${}'.format(dist * 0.5))
else:
    print('O valor da sua passagem será: ${}'.format(dist * 0.45))