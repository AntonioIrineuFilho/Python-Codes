n = int(input())
seq = []
q = 0
for i in range(0, n):
    x = int(input())
    seq.append(x)

for j in range(len(seq)):
    if (j == 0):
        q = q + 1
    elif (j == len(seq)-1):
        q = q + 1
    elif (seq[j-1] != seq[j+1]):
        q = q + 0
    else:
        q = q + 1

print(q)