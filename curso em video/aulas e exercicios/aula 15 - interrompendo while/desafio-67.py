li = ['S', 'ss', 's', 'SS', 'sim', 'Sim', 'SIM']
li2 = ['N', 'nn', 'n', 'NN', 'nao', 'não', 'Não', 'Nao', 'NÃO', 'NAO']

while True:
    n = int(input('Digite um valor: '))
    cont = 1
    while cont != 11:
        print(f'{n} x {cont} = {n*cont}')
        cont = cont + 1
    x = input('Deseja continuar? [S/N] ').strip()
    if (x in li2):
        print('-FIM-')
        break
    while (x not in li) and (x not in li2):
            x = input('Desculpe, não entendi. Você deseja continuar? ')
            if (x in li2):
                break
    if (x in li2):
        print('-FIM-')
        break
        

    