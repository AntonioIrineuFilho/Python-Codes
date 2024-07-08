def sublista_sem_menor(lista):
    lista2 = list(lista)
    indice = lista2.index(sorted(lista2)[0])
    del(lista2[indice])
    lista2 = ' '.join(lista2)
    return lista2

l = list(map(str, input().split()))

print(sublista_sem_menor(l))