import random

jogadores = dict()
jogadores_copia = jogadores.copy()
s = 1
for i in range(1, 5):
    jogadores[f'Jogador{i}'] = random.randint(1, 6)

for j in jogadores:
    maior = 0
    for k, l in jogadores_copia.items():
        if (l >= maior):
            maior = l
            jog = k
    print(f'{s} Lugar: {jog} com o número {maior}')
    s = s + 1
    del(jogadores_copia[jog])