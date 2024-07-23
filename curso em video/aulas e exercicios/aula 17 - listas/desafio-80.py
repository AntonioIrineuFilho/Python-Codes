lista = []

for i in range(0, 5):
    n = int(input(f'Digite o número {i+1}º: '))
    if (i == 0):
        lista.append(n)
    if (i == 1):
        if (n >= lista[0]):
            lista.append(n)
        else:
            n_anterior = lista[0]
            lista[0] = n
            lista.append(n_anterior)
    if (i == 2):
        if (n >= lista [1]):
            lista.append(n)
        elif (n >= lista[0]):
            n_anterior = lista[1]
            lista[1] = n
            lista.append(n_anterior)
        else:
            n_anterior = lista[0]
            n_anterior2 = lista[1]
            lista[0] = n
            lista[1] = n_anterior
            lista.append(n_anterior2)
    if (i == 3):
        if (n >= lista[2]):
            lista.append(n)
        elif (n >= lista[1]):
            n_anterior = lista[2]
            lista[2] = n
            lista.append(n_anterior)
        elif (n >= lista[0]):
            n_anterior = lista[1]
            n_anterior2 = lista[2]
            lista[1] = n
            lista[2] = n_anterior
            lista.append(n_anterior2)
        else:
            n_anterior = lista[0]
            n_anterior2 = lista[1]
            n_anterior3 = lista[2]
            lista[0] = n
            lista[1] = n_anterior
            lista[2] = n_anterior2
            lista.append(n_anterior3)
    if (i == 4):
        if (n >= lista[3]):
            lista.append(n)
        elif (n >= lista[2]):
            n_anterior = lista[3]
            lista[3] = n
            lista.append(n_anterior)
        elif (n >= lista[1]):
            n_anterior = lista[2]
            n_anterior2 = lista[3]
            lista[2] = n
            lista[3] = n_anterior
            lista.append(n_anterior2)
        elif (n >= lista[0]):
            n_anterior = lista[1]
            n_anterior2 = lista[2]
            n_anterior3 = lista[3]
            lista[1] = n
            lista[2] = n_anterior
            lista[3] = n_anterior2
            lista.append(n_anterior3)
        else:
            n_anterior = lista[0]
            n_anterior2 = lista[1]
            n_anterior3 = lista[2]
            n_anterior4 = lista[3]
            lista[0] = n
            lista[1] = n_anterior
            lista[2] = n_anterior2
            lista[3] = n_anterior3
            lista.append(n_anterior4)

print(lista)


