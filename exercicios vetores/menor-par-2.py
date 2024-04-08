li = list(map(int, input().split()))
x = []
for a in range(len(li)):
    if (li[a] % 2 == 0):
        x.append(li[a])
if (x == []):
    print('Não há números pares nessa lista')
else:
    y = sorted(x)
    print('O menor par dessa lista é o número {}'.format(y[0]))