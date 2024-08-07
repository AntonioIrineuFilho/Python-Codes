max_trocos = []
q = int(input())
for i in range(0, q):
    valor_ini, quant_marcas = map(int, input().split())
    precos = list(map(float, input().split()))
    maior = 0
    for j in range(len(precos)):
        troco = valor_ini % precos[j]
        if (troco >= maior):
            maior = troco
        if (j == len(precos)-1):
            max_trocos.append(maior)

for k in max_trocos:
    print(f'{k:.2f}')
