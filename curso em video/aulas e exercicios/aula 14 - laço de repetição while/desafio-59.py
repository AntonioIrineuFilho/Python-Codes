n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('-'*30)
print('Escolha uma das opções abaixo:')
print('-'*30)
print('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair')
x = int(input('Digite a opção desejada: '))
if (x == 1):
    print('A soma dos números {} e {} é {}'.format(n1, n2, n1+n2))
elif (x == 2):
    print('O produto dos números {} e {} é {}'.format(n1, n2, n1*n2))
elif (x == 3):
    print('O maior valor entre {} e {} é {}'.format(n1, n2, max(n1, n2)))
elif (x == 4):
    n1 = int(input('Digite o novo primeiro valor: '))
    n2 = int(input('Digite o novo segundo valor: '))

while x != 5:
    print('-'*20)
    print('O que fazer agora?')
    print('-'*20)
    print('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair')
    x = int(input('Digite a opção desejada: '))
    if (x == 1):
        print('A soma dos números {} e {} é {}'.format(n1, n2, n1+n2))
    elif (x == 2):
        print('O produto dos números {} e {} é {}'.format(n1, n2, n1*n2))
    elif (x == 3):
        print('O maior valor entre {} e {} é {}'.format(n1, n2, max(n1, n2)))
    elif (x == 4):
        n1 = int(input('Digite o novo primeiro valor: '))
        n2 = int(input('Digite o novo segundo valor: '))

print('-FIM-')
