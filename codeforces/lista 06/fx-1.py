def maior(x, y, w, z):
    if (x >= y and x >= w and x >= z):
        return x
    elif (y >= w and y >= z):
        return y
    elif (w >= z):
        return w
    else:
        return z

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

print(f'O maior valor digitado é {maior(n1, n2, n3, n4)}')