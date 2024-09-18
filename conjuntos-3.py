s = [1, 2, 3, 4]
rel = [(1, 2), (2, 3), (4, 4)]
prod_cart = []

for i in s:
    for j in s:
        prod_cart.append((i, j))

for i in rel:
    if (i in prod_cart):
        indice = prod_cart.index(i)
        del(prod_cart[indice])

print(f'Complemento da relação: {prod_cart}')
        