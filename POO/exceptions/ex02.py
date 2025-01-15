lista = []

for i in range(0, 10):
    lista.append(i)

try:
    print(lista[10])
except IndexError:
    raise IndexError("INDEX OUT OF BOUND")
