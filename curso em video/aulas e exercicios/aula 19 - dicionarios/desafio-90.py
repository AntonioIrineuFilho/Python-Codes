alunos = []

while True:
    nome = input('Digite o nome: ').strip().upper()
    media = float(input('Digite a média: '))
    situ = input('Digite a situação(Aprovado, Em Recuperação ou Reprovado): ').strip().upper()
    alunos.append({'Nome':nome, 'Média':media, 'Situação':situ})
    op = input('Deseja continuar [S/N]? ').strip().upper()
    while True:
        if (op == 'S' or op == 'N'):
            break
        else:
            op = input('Opção inválida. Digite S para continuar ou N para encerrar: ').strip().upper()
    if (op == 'N'):
        break

for i in alunos:
    for j, k in i.items():
        print(f'{j} do(a) aluno(a) é {k}')