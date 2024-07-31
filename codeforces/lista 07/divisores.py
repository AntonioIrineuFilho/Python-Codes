n = int(input())
d = 1
while True:
    if (n % d == 0):
        print(f'{d}', end=' ')
    d = d + 1
    if (d > n):
        break