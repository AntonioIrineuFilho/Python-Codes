ln = [[], []]

for i in range(0, 7):
    n = int(input(f'Digite o {i+1} número: '))
    if (n % 2 == 0):
        ln[0].append(n)
    else:
        ln[1].append(n)

print(f'Os valores pares digitados foram: {sorted(ln[0])}')
print(f'Os valores impares digitados foram: {sorted(ln[1])}')