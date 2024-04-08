li = list(map(int, input().split()))
for a in range(len(li)):
    if (li[a] % 2 == 0):
        print('Os números pares da lista são: ', end = "")
        break
for b in range(len(li)):
    if (li[b] % 2 == 0):
        print(li[b], end = " ")
if not (li[b] % 2 == 0):
    print('Essa lista não possui números pares')
    