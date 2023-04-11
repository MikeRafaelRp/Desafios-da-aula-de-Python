from random import randint
rand = randint(0,5)
chute = int(input('Tente acertar o número aleátorio de 0 a 5: '))
if chute == rand:
    print('Você acertou Parabéns!')
else:
    print('Você errou, que pena...')
