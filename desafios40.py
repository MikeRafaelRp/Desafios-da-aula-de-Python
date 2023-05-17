nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if 7 > media >= 5:
    print('''
          MÉDIA: {:.1f} RECUPERAÇÃO'''.format(media))
elif media < 5:
    print('''
          MÉDIA: {:.1f} REPROVADO'''.format(media))
elif media >= 7:
    print('''
          MÉDIA: {:.1f} APROVADO'''.format(media))