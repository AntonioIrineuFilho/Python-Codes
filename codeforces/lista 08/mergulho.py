n, r = map(int, input().split())
lr = list(map(int, input().split()))
ln = []
lm = []
if (n == r):
    print('*')
else:
    for i in range(1, n+1):
        ln.append(i)
    for j in range(len(ln)):
        if (ln[j] not in lr):
            lm.append(ln[j])

for k in lm:
    print(k, end=' ')
    
