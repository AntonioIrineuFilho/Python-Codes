import time

print('Digite os 20 times do Brasileirão Serie A em ordem decrescente de pontuação:')
tabela = tuple(map(str, input().strip().upper().split()))
opv = (1, 2, 3, 4, 5)

while True:
    print('-'*34)
    print('Opções:')
    print('1- 5 primeiro colocados\n2- 4 últimos colocados\n3- Ordem alfabética\n4- Colocação de um time específico\n5- Sair')
    print('-'*34)
    x = int(input('Digite a opção escolhida: '))
    while True:
            if (x in opv):
                break
            else:
                x = int(input('Opção inválida. Digite uma opção válida: '))
    if (x == 1):
        print('Os 5 primeiros colocados são: ', end='')
        print(*tabela[0:5], sep=', ')
        time.sleep(1)
    elif (x == 2):
        print('Os 4 últimos colocados são: ', end='')
        print(*tabela[(len(tabela) - 4):(len(tabela))], sep=', ')
        time.sleep(1)
    elif (x == 3):
        print('Ordem alfabética:')
        print(*sorted(tabela), sep=', ')
        time.sleep(1)
    elif (x == 4):
        team = input('Digite o time desejado: ').strip().upper()
        while True:
            if (team in tabela):
                break
            else:
                team = input('Time inválido. Digite um time válido: ').strip().upper()
        print(f'O {team} está na {tabela.index(team)+1} colocação da tabela')
        time.sleep(1)
    else:
        print('-FIM-')
        break


