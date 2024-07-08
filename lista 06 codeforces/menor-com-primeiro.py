def lista_troca_menor_primeiro(lista: list):
    pe = lista[0]
    me = sorted(lista)[0]
    me_indice = lista.index(me)
    lista[0] = me
    lista[me_indice] = pe
    if (pe == me):
        return 0
    else:
        return 1

l = list(map(str, input().split()))

print(lista_troca_menor_primeiro(l))