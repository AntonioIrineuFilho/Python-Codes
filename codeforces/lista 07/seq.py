n = int(input())
seq = []
q = 0
for i in range(0, n):
    x = int(input())
    seq.append(x)

for j in range(len(seq)):
    if (j == len(seq)-1):
        q = q + 1
    elif not (seq[j] == seq[j+1]):
        q = q + 1

print(q)
    