a = list(map(int, input().split()))
seq = []
q = 0

for i in range(len(a)):
    if (a[i] == 0):
        q = q + 1
    else:
        if (q > 0):
            for j in range(0, q):
                seq.append(q)
            q = 0
            seq.append(q)
        else:
            seq.append(q)

print(*seq)