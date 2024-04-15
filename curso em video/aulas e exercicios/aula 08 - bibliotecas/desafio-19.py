import random
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
n = random.randint(1,4)
if (n == 1):
    print('{} foi o sorteado!'.format(a1))
elif (n == 2):
    print('{} foi o sorteado!'.format(a2))
elif (n == 3):
    print('{} foi o sorteado!'.format(a3))
else:
    print('{} foi o sorteado!'.format(a4))
    