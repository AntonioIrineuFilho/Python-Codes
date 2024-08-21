testes = []

while True:
    lx = []
    x = input().strip().upper().split()
    if (x[0] == '*'):
        break
    for i in range(len(x)):
        p = x[i]
        lx.append(p[0])
    if (lx.count(lx[0]) == len(lx)):
        testes.append('Y')
    else:
        testes.append('N')

for j in testes:
    print(j)