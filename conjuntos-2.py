rel = [(1, 2), (1, 3), (2, 1), (3, 1), (2, 4), (4, 2), (4, 1), (1, 4)]
a = []
b = []

for (x, y) in rel:
    if (x == 1):
        a.append(y)
for (x, y) in rel:
    if (x == 2):
        if (y in a):
            b.append(y)

print(a)
print(b)

