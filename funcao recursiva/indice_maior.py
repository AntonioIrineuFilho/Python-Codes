maior = 0

def b_index_ini(lista, tamanho, inicial):
    global maior
    if (inicial == tamanho):
        return lista.index(maior)
    else:
        if (lista[inicial] >= maior):
            maior = lista[inicial]
            return b_index_ini(lista, tamanho, inicial+1)
        else:
            return b_index_ini(lista, tamanho, inicial+1)



def b_index(lista):
    return b_index_ini(lista, len(lista), 0)

lista = list(map(int, input().split()))

print(f'O maior número da lista é {lista[b_index(lista)]} e está na posição {b_index(lista)+1}')