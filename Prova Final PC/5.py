n = list(map(int, input().split()))

pos = []
neg = []
nulos = []

for i in n:
    if (i > 0):
        pos.append(i)
    elif (i < 0):
        neg.append(i)
    else:
        nulos.append(i)

print(f'Existem {len(pos)} positivos e são: {pos}')
print(f'Existem {len(neg)} negativos e são: {neg}')
print(f'Existem {len(nulos)} nulos e são: {nulos}')