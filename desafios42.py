r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceria reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podem formar um triângulo!', end='')
    if r1 != r2 != r3 != r1:
        print('Triângulo Escaleno.')
    elif r1 == r2 == r3:
        print('Triângulo Equilátero.')
    else:
        print('Triângulo Isósceles.')
else:
    print('Não podem formar um triângulo!')
