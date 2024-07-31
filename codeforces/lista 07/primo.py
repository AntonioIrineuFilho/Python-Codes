n = int(input())
d = n-1
while True:
    if (n == 1):
        print('Nao')
        break
    elif (d == 1):
        print('Sim')
        break
    elif (n % d == 0):
        print('Nao')
        break
    d = d - 1