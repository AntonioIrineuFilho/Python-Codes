a, b = map(int, input().split())
m = 0
while True:
    m = m + a
    if (m <= b):
        print(f'{m}', end=' ')
    if (m >= b):
        break
