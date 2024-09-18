li = list(map(int, input().split()))
x = []
for a in range(len(li)):
    if (li[a] % 2 == 0):
        x.append(li[a])
if not (x == []):
    print('A lista possui {} números pares, que são: {}'.format(len(x), x))
else:
    print('A lista não possui números pares')