alunos = []

while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    alunos.append([nome, n1, n2])
    op = int(input('Digite 1 para continuar e 0 para encerrar: '))
    while True:
        if (op == 1 or op == 0):
            break
        else:
            op = int(input('Opção inválida. Digite 1 para continuar e 0 para encerrar: '))
    if (op == 0):
        break

print('No. Nome   Média')
for i in range(len(alunos)):
    print(f'{i} {alunos[i][0]}  {(alunos[i][1]+alunos[i][2])/2:.1f}')

while True:
    n = int(input('Digite o número do aluno desejado ou 999 para encerrar:'))
    while True:
        if (n == 999):
            break
        elif (n > len(alunos)-1 or n < 0):
            n = int(input('Aluno não encontrado. Digite um número válido ou 999 para encerrar:'))
        else:
            print(f'Nome: {alunos[n][0]}\nNotas: {alunos[n][1]} e {alunos[n][2]}\nMédia: {(alunos[n][1]+alunos[n][2])/2:.1f}')
            break
    if (n == 999):
        break
        