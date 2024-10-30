n = int(input())
b = []
x = ''

while n > 0:
    b.append(str(n % 2))
    n = n // 2

for i in range(len(b)):
    x = x + b[len(b)-(i+1)]

print(x)