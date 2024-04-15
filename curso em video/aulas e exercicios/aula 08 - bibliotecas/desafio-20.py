import random
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
li = [a1, a2, a3, a4]
li2 = random.sample(li, k=4)
print('A ordem sorteada foi = ', end = '')
print('{ ', end = '')
print(*li2, sep=', ', end = '')
print(' }')