import math

n = int(input())
ln = []
s = 0

for i in range(0, n):
    b = int(input())
    ln.append(b)

media = sum(ln)//n

for j in range(len(ln)):
    dif = math.ceil((100 * ln[j]) / media)
    if (dif - 100 < 0):
        if ((dif - 100) * (-1) > 10):
            s = s + 1
    else:
        if (dif - 100 > 10):
            s = s + 1

print(f'{media}\n{s}')