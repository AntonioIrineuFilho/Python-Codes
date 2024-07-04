def lista_troca_menor_primeiro(lista):
    lista = list(lista)
    pe = lista[0]
    me = sorted(lista)[0]
    me_indice = lista.index(me)
    lista[0] = me
    lista[me_indice] = pe
    if (pe == me):
        t = 0
    else:
        t = 1
    ld = ' '.join(lista)
    return f'{t}\n{ld}'

l = list(map(str, input().split()))

print(lista_troca_menor_primeiro(l))