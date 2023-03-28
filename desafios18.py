from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hyp = hypot(co,ca)
print('O comprimento do cateto oposto é: {:.2f}, e do adjacente é de: {:.2f}, calculando os dois a sua hipotenusa é: {:.2f}'.format(co,ca,hyp))