print('-' * 19)
print('Conversor de Bases')
print('-' * 19)
n = int(input('Digite o valor: '))
print('Opções de Conversão:')
print('[ 1 ]Binário\n[ 2 ]Octal\n[ 3 ]Hexadecimal')
op = int(input('Digite a opção da conversão desejada: '))

if (op == 1):
    print('{} convertido em binário é {}'.format(n, bin(n)[2:]))
elif (op == 2):
    print('{} convertido em octal é {}'.format(n, oct(n)[2:]))
elif (op == 3):
    print('{} convertido em hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida')