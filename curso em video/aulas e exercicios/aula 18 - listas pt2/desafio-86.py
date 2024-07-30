ln = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite um valor para [{i}, {j}]: '))
        ln[i].append(n)

for i in range(0, 3):
    for j in range(0, 3):
        if (j == 2):
            print(f'[ {ln[i][j]} ]')
        else:
            print(f'[ {ln[i][j]} ]', end=' ')