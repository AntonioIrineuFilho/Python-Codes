l = [1, 2, 3, 4, 5]
cont = 1
p = 1
def produto(lista: list):
    global cont
    global p
    if (cont == len(lista)):
        return p
    p = p * lista[cont]
    cont = cont + 1
    return produto(l)

print(produto(l))