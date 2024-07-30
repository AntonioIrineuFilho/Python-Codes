s = [1, 2, 3, 4]
p_cart = []
paridade = []

for i in s:
    for j in s:
        if ((i, j) not in p_cart):
            p_cart.append((i, j))

for (i, j) in p_cart:
    if (i % 2 == 0 and j % 2 == 0):
        paridade.append((i, j))
    if (i % 2 != 0 and j % 2 != 0):
        paridade.append((i, j))

print(paridade)