testes = []

while True:
    maior_x1 = -10000
    maior_y2 = -10000
    menor_y1 = 10000
    menor_x2 = 10000
    n = int(input())
    if (n == 0):
        break
    for i in range(0, n):
        x1, y1, x2, y2 = map(int, input().split())
        if (x1 >= maior_x1):
            maior_x1 = x1
        if (y1 <= menor_y1):
            menor_y1 = y1
        if (x2 <= menor_x2):
            menor_x2 = x2
        if (y2 >= maior_y2):
            maior_y2 = y2 
    testes.append([maior_x1, menor_y1, menor_x2, maior_y2])

for j in range(len(testes)):
    if (j == 0):
        if (testes[j][0] < testes[j][2] and testes[j][1] > testes[j][3]):
            print(f'Teste {j+1}')
            print(*testes[j])
        else:
            print(f'Teste {j+1}')
            print('nenhum')
    else:
        if (testes[j][0] < testes[j][2] and testes[j][1] > testes[j][3]):
            print(f'\nTeste {j+1}')
            print(*testes[j]) 
        else:
            print(f'\nTeste {j+1}')
            print('nenhum')   