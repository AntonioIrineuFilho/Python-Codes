q = 0
s = 0

while True:
    n = int(input('Digite um valor: '))
    if (n != 999):
        q = q + 1
        s = s + n
    else:
        break

print(f'Foram digitados {q} números')
print(f'A soma dos números digitados é {s}')