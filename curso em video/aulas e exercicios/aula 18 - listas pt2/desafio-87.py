matriz = [[], [], []]
sp = 0
stc = 0
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite o valor da posição [{i}] [{j}]: '))
        matriz[i].append(n)
        if (n % 2 == 0):
            sp = sp + n

for i in range(0, 3):
    for j in range(0, 3):
        if (j == 2):
            print(f'[ {matriz[i][j]} ]')
            stc = stc + matriz[i][j]
        else:
            print(f'[ {matriz[i][j]} ]', end=' ')


print(f'Soma dos pares: {sp}')
print(f'Soma dos valores da terceira coluna: {stc}')
print(f'Maior valor da segunda linha: {max(matriz[1])}')

