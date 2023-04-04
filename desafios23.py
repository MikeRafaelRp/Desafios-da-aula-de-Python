num = str(input('Digite um número de 0 a 9999 '))
unidade = num[3]
dezena = num[2]
centena = num[1]
milhar = num[0]
print('Número digitado foi: {} separando fica da seguinte forma: {} unidade, {} dezena, {} centena e {} milhar'.format(num,unidade,dezena,centena,milhar))