r = [(1, 1), (1, 2), (2, 2), (2, 3), (3, 1), (3, 3), (4, 1)]
s = [(1, 1), (2, 1), (2, 2), (3, 1)]
comp = []

for (a, b) in r:
    for (c, d) in s:
        if (b == c):
            if ((a, d) not in comp):
                comp.append((a, d))

print(comp)