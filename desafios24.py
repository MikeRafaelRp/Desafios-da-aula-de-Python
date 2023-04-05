cidade = str(input('Digite o nome de uma Cidade: ')).strip()
print('A cidade que você digitou começa com Santo: {}'.format(cidade[:5].upper() == 'SANTO'))