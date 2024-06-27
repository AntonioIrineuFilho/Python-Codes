import time

v = ['a', 'e', 'i', 'o', 'u']
c = ['b', 'c', 'ç', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
opv = [1, 2, 3]
lp = list(map(str, input('Digite várias palavras(sem acento e separadas por espaço):\n').strip().lower().split()))

while True:
    time.sleep(0.5)
    print('-'*20)
    print('Opções:')
    print('1- Ver as vogais\n2- Ver as consoantes\n3- Sair')
    print('-'*20)
    op = int(input('Escolha uma opção: '))
    while True:
        if (op in opv):
            break
        else:
            op = int(input('Opção inválida. Escolha uma opção válida: '))
    if (op == 1):
        for x in range(len(lp)):
            liv = []
            for y in range(len(lp[x])):
                p = lp[x]
                if (p[y] in v):
                    liv.append(p[y])
            if (len(liv) != 0):
                print(f'A palavra {lp[x].upper()} possui as vogais', '{', end='')
                print(*liv, sep=', ', end='')
                print('}')
            else:
                print(f'A palavra {lp[x].upper()} não possui vogais')
    elif (op == 2):
        for x in range(len(lp)):
            lic = []
            for y in range(len(lp[x])):
                p = lp[x]
                if (p[y] in c):
                    lic.append(p[y])
            if (len(lic) != 0):
                print(f'A palavra {lp[x].upper()} possui as consoantes', '{', end='')
                print(*lic, sep=', ', end='')
                print('}')
            else:
                print(f'A palavra {lp[x].upper()} não possui consoantes')
    else:
        print('-FIM-')
        break



            
            

    



