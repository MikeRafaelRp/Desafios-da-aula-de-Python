nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 5 and media <= 6.9:
    print('''
          MÉDIA: {} RECUPERAÇÃO'''.format(media))
elif media < 5:
    print('''
          MÉDIA: {} REPROVADO'''.format(media))
elif media > 7:
    print('''
          MÉDIA: {} APROVADO'''.format(media))