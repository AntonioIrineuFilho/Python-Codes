q = int(input())
testes = []
for i in range(0, q):
    n = float(input())
    testes.append(n)

for j in range(len(testes)):
    estoque = testes[j]
    dias = 0
    while True:
        if (estoque <= 1.0):
            print(f'{dias} dias')
            break
        estoque = estoque / 2
        dias = dias + 1

