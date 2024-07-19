def ocorrencias_ini(lista, x, tamanho, inicial):
    if (inicial == tamanho):
        return 0
    else:
        if (lista[inicial] == x):
            return 1 + ocorrencias_ini(lista, x, tamanho, inicial+1)
        else:
            return 0 + ocorrencias_ini(lista, x, tamanho, inicial+1)

def ocorrencias(lista, x):
    return ocorrencias_ini(lista, x, len(lista), 0)

lista = list(map(int, input().split()))
x = int(input())

print(f'O número {x} possui {ocorrencias(lista, x)} ocorrências na lista')