a = list(map(int, input('Digite o conjunto 1: ').split()))
b = list(map(int, input('Digite o conjunto 2: ').split()))

inter = []
dif = []

if (len(a) > len(b)):
    maior = a
    menor = b
else:
    maior = b
    menor = a

if (len(a) != len(b)):
    for i in menor:
        if (i in maior):
            inter.append(i)
        else:
            dif.append(i)
    for j in maior:
        if (j not in menor):
            dif.append(j)
else:
    for i in a:
        if (i in b):
            inter.append(i)
        else:
            dif.append(i)
    for j in b:
        if (j not in a):
            dif.append(j)

print(f'Intersecção: {inter}')
print(f'Diferença: {dif}')
print(f'União: {inter+dif}')