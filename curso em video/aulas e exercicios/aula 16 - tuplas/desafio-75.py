import time

tupla = tuple(map(int, input('Digite vários números(sepados por espaço): ').split()))
opv = (1, 2, 3, 4, 5, 6)

while True:
    time.sleep(1)
    print('-'*35)
    print('Opções:')
    print('1- Quantas vezes aparece um número\n2- Primeira aparição de um número\n3- Quais são os números pares\n4- Quais são os números ímpares\n5- Nova tupla\n6- Sair')
    print('-'*35)
    x = int(input('Digite sua escolha: '))
    while True:
        if (x in opv):
            break
        else:
            x = int(input('Opção inválida. Digite uma opção válida: '))
    if (x == 1):
        n = int(input('Digite o número desejado: '))
        if (tupla.count(n) == 0):
            print(f'O número {n} não está na tupla')
        else:
            print(f'O número {n} aparece {tupla.count(n)} vezes na tupla')
    elif (x == 2):
        n2 = int(input('Digite o número desejado: '))
        if (tupla.count(n2) == 0):
            print(f'O número {n2} não está na tupla')
        else:
            print(f'A primeira aparição do número {n2} ocorre na posição {tupla.index(n2)+1}')
    elif (x == 3):
        pares = 0
        print('Os números pares da tupla são: ', end='')
        for a in range(len(tupla)):
            if (tupla[a] % 2 == 0):
                pares = pares + 1
                print(f'{tupla[a]} ', end='')
        if (pares != 0):
            print('\n')
        else:
            print('none\n')
    elif (x == 4):
        impares = 0
        print('Os números ímpares da tupla são: ', end='')
        for b in range(len(tupla)):
            if not (tupla[b] % 2 == 0):
                impares = impares + 1
                print(f'{tupla[b]} ', end='')
        if (impares != 0):
            print('\n')
        else:
            print('none\n')
    elif (x == 5):
        tupla = tuple(map(int, input('Digite vários números(sepados por espaço): ').split()))
    else:
        print('-FIM-')
        break
