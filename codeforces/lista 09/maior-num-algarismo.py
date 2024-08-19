decimais = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
testes = []

while True:
    n1, n2 = map(int, input().split())
    if (n1 == 0 and n2 == 0):
        break
    while True:
        ln1 = []
        while n1 > 0:
            ln1.append(n1 % 10)
            n1 = n1 // 10
        n1 = sum(ln1)
        if (n1 in decimais):
            break
    while True:
        ln2 = []
        while n2 > 0:
            ln2.append(n2 % 10)
            n2 = n2 // 10
        n2 = sum(ln2)
        if (n2 in decimais):
            break
    if (n1 > n2):
        testes.append(1)
    elif (n1 == n2):
        testes.append(0)
    else:
        testes.append(2)

for i in testes:
    print(i)