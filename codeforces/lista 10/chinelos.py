n = int(input())
nv = 0
quant_tam = []

for i in range(0, n):
    x = int(input())
    quant_tam.append(x)

np = int(input())

for j in range(0, np):
    p = int(input())
    if (quant_tam[p-1] > 0):
        nv = nv + 1
        quant_tam[p-1] = quant_tam[p-1] - 1

print(nv)
