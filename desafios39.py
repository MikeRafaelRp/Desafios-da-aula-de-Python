from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano em que você nasceu: '))
idade = atual - nasc
if idade == 18:
    print('É hora de você se alistar.')
elif idade > 18:
    print('Já passou {} anos que você devia se alistar.'.format(idade - 18))
elif idade < 18:
    print('Falta {} anos para você poder se alistar.'.format(18 - idade ))
    