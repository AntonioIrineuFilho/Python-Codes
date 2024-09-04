n = int(input())
posicoes = []

for i in range(0, n):
    d, b, r, c = map(int, input().split())
    posicoes_ini = [(r, c)]
    if (d == 0):
        for j in range(r+1, c+b):
            c = c + 1
            posicoes_ini.append((r, c))
    else:
        for j in range(r+1, r+b):
            posicoes_ini.append((j, c))
    posicoes.append(posicoes_ini)

for k in range(len(posicoes)):
    navio = posicoes[k]
    for l in range(len(navio)):
        coord = navio[l]
        if ((coord[0] > 10 or coord[0] < 1) or (coord[1] > 10 or coord[1] < 1)):
            print('N')
            quit()
        for m in range(len(posicoes)):
            if (coord in posicoes[m] and m != k):
                print('N')
                quit()
    if (k == len(posicoes)-1):
        print('Y')