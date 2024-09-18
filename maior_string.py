lista = list(map(str, input('Digite as palavras: ').strip().split()))

def maior_string(lista):
    maior = ''
    for i in range(len(lista)):
        if (len(lista[i]) > len(maior)):
            maior = lista[i]
    maiores = [maior]
    for j in range(len(lista)):
        if (len(lista[j]) == len(maior) and lista[j] != maior):
            maiores.append(lista[j])
    return maiores

def menor_string(lista):
    menor = lista[0]
    for i in range(len(lista)):
        if (len(lista[i]) < len(menor)):
            menor = lista[i]
    menores = [menor]
    for j in range(len(lista)):
        if (len(lista[j]) == len(menor) and lista[j] != menor):
            menores.append(lista[j])
    return menores

print(maior_string(lista))
print(menor_string(lista))