lista = list(map(int, input().split()))
lista_copia = lista.copy()

for i in range(lista.count(max(lista))):
    lista_copia.remove(max(lista_copia))

print(max(lista_copia))