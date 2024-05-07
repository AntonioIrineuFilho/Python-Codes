n = int(input('Digite um número inteiro: '))
li = []
for i in range(2, n):
    if (n % i == 0):
        li.append(i)

if (len(li) == 0):
    print('{} é primo'.format(n))
else:
    print('{} não é primo e possui {} divisores além de 1 e ele mesmo'.format(n, len(li)))
    print('Os divisores de {} são = {}'.format(n, li))