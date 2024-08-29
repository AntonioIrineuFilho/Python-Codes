comp, min_pontos = map(int, input().split())
conv = 0

for i in range(0, comp):
    f1, f2 = map(int, input().split())
    if (f1 + f2 >= min_pontos):
        conv = conv + 1

print(conv)