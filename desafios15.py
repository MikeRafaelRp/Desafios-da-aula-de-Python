dias = int(input('Por quantos dias você quer alugar esse carro? '))
km = float(input('E por quantos kilometros? '))
aluguel = (dias * 60) + (km * 0.15)
print('O preço a pagar é: R${:.2f}'.format(aluguel))