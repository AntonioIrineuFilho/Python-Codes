n = int(input())
min_class = int(input())
ln = []
classificados = []

for i in range(0, n):
    notas = int(input())
    ln.append(notas)

ln2 = sorted(ln)

for j in range(0, min_class):
    classificados.append(ln2[len(ln2)-(j+1)])

ult_num = classificados[-1]

if (ln.count(ult_num) > 1):
    for k in range(classificados.count(ult_num), ln.count(ult_num)):
        classificados.append(ult_num)

print(len(classificados))