q = int(input())
ln = list(map(int, input().split()))
media = sum(ln) / q
acima = 0
abaixo = 0

for i in ln:
    if (i < media):
        abaixo = abaixo + 1
    else:
        acima = acima + 1

print(f'{media:.1f}\n{abaixo}\n{acima}')




