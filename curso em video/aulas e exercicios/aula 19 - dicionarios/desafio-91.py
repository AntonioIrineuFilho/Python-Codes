import random

jogadores = dict()
jogadores_copia = jogadores.copy()

for i in range(1, 5):
    jogadores[f'Jogador{i}'] = random.randint(1, 6)

for j in range(len(jogadores)):
    maior = 0
    for k, l in jogadores_copia.items():
        if (l >= maior):
            maior = l
            jog = k
    print(f'{j+1} Lugar: {jog} com o número {maior}')
    del(jogadores_copia[jog])
    del(jogadores_copia[maior])