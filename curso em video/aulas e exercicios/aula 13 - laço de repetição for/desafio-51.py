print('-*' * 22)
print('CALCULANDO OS 10 PRIMEIROS TERMOS DE UMA PA')
print('-*' * 22)

n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
li = []

for i in range(n, n + 10 * r, r):
    li.append(i)
for a in range(len(li)):
    print('O termo {} é {}'.format((a+1), li[a]))