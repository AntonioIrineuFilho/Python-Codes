pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
n = 1

while n != 11:
    nt = pt + (n - 1) * r
    print(nt)
    n = n + 1

x = int(input('Digite quantos termos a mais você deseja: '))
y = n

while x != 0:
    while (x + y) != n:
        nt = pt + (n - 1) * r
        print(nt)
        n = n + 1
    x = int(input('Digite quantos termos a mais você deseja: '))
    y = n

print('-FIM-')