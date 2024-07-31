q = int(input())
ln = list(map(int, input().split()))
media = sum(ln) / q
abaixo = []
acima = []
for i in ln:
    if (i < media):
        abaixo.append(i)
    else:
        acima.append(i)
print(f'{media:.1f}')
print(len(abaixo), *abaixo)
print(len(acima), *acima)