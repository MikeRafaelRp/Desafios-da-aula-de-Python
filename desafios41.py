from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano que você nasceu: '))
idade = atual - nasc
if idade <= 9:
    print('''
          MIRIM''')
elif idade <= 14:
    print('''
          INFANTIL''')
elif idade <= 19:
    print('''
          JUNIOR''')
elif idade == 20:
    print('''
          SÊNIOR''')
else:
    print('''
          MASTER''')