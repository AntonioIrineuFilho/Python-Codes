lista = []

for i in range(0, 5):
    n = int(input())
    lista.append(n)

mediano = sorted(lista)[2]
med_indice = lista.index(mediano)
del(lista[med_indice])

print(sum(lista)/len(lista))