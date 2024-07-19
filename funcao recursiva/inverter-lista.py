def inverter_ini(lista_inv, tamanho, inicial):
    if (inicial == tamanho//2):
        return lista_inv
    else:
        t1 = lista_inv[inicial]
        t2 = lista_inv[len(lista_inv)-inicial-1]
        lista_inv[inicial] = t2
        lista_inv[len(lista_inv)-inicial-1] = t1
        return inverter_ini(lista_inv, tamanho, inicial+1)
    
def inverter(lista_inv):
    return inverter_ini(lista_inv, len(lista_inv), 0)

lista = list(map(int, input().split()))
lista_inv = lista.copy()

print(inverter(lista_inv))