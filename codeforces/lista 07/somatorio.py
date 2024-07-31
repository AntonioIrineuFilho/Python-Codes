n = int(input())
s = 0
while True:
    s = s + (1/n)
    n = n - 1
    if (n == 0):
        break
print(f'{s:.4f}')