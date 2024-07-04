def sublista_sem_menor(lista):
    lista2 = list(lista)
    indice = lista2.index(sorted(lista2)[0])
    del(lista2[indice])
    return f'{lista}\n{lista2}'

l = list(map(int, input().split()))

print(sublista_sem_menor(l))