s = 0

def sum_pares_ini(lista, tamanho, inicial):
    global s
    if (inicial == tamanho):
        return s
    else:
        if (lista[inicial] % 2 == 0):
            s = s + lista[inicial]
            return sum_pares_ini(lista, tamanho, inicial+1)
        else:
            return sum_pares_ini(lista, tamanho, inicial+1)

def sum_pares(lista):
    return sum_pares_ini(lista, len(lista), 0)

lista = list(map(int, input().split()))

print(sum_pares(lista))