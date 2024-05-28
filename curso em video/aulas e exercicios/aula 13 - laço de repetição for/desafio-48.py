s = 0
x = 0

for i in range(1, 501, 2):
    if (i % 3 == 0):
        s = s + i
        x = x + 1

print('A soma dos {} valores foi {}'.format(x, s))