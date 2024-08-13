import random

n = int(input('Quanos jogos devem ser gerados? '))
jogos = []

for i in range(0, n):
    lx = []
    for j in range(0, 6):
        x = random.randint(1, 60)
        while True:
            if (x in lx):
                x = random.randint(1, 60)
            else:
                lx.append(x)
                break
    jogos.append(lx)

for k in range(len(jogos)):
    print(f'Jogo {k+1}: {jogos[k]}')