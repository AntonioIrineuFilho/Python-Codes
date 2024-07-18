anterior = 0

def lista_ordenada_ini(lista, tamanho, inicial):
    global anterior
    if (inicial == tamanho):
        return True
    else:
        if (lista[inicial] >= anterior):
            anterior = lista[inicial]
            return lista_ordenada_ini(lista, tamanho, inicial+1)
        else:
            return False
        
def lista_ordenada(lista):
    return lista_ordenada_ini(lista, len(lista), 0)

lista = list(map(int, input().split()))

print(lista_ordenada(lista))