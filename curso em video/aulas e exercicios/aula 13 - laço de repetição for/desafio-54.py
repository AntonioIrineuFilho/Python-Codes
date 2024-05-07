x = 0
y = 0
for i in range (0, 7):
    n = int(input('Digite uma idade: '))
    if (n < 21):
        x = x + 1
    else:
        y = y + 1
print('Existem {} menores de idade e {} maiores de idade'.format(x, y))
