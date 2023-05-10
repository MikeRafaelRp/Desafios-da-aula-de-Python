num = int(input('Digite um número inteiro: '))
escolha = int(input('''Escolha a base de conversão: 
                            [1] para Binário 
                            [2] para Octal 
                            [3] para Hexadecimal'''))
if escolha == 1:
    print('O número inteiro que você escolheu {} ,convertido para Binário ficou: {}'.format(num,bin(num)[2:]))
elif escolha == 2:
    print('O número inteiro que você escolheu {} ,convertido para Octal ficou: {}'.format(num,oct(num)[2:]))
elif escolha == 3:
    print('O número inteiro que você escolheu {} ,convertido para Hexadecimal ficou: {}'.format(num,hex(num)[2:]))
else:
    print('Digite um número válido...')
