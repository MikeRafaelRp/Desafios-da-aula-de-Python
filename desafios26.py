frase = str(input('Digite uma frase: '))
print('Aparece {} vezes a letra A, a primeira vez que aparece a letra A é na posição: {}, e a ultima vez é: '.format(frase.count('A'),frase.find('A')))