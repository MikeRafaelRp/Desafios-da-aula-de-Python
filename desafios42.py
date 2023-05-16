r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceria reta: '))
if r1 != r2 and r1 != r3 and r2 != r3:
    print('Triângulo Escaleno.')
elif r1 == r2 and r1 == r3 and r2 == r3:
    print('Triângulo Equilátero.')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('Triângulo Isósceles.')