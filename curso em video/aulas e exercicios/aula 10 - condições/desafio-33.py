n1, n2, n3 = map(int, input('Digite três números inteiros: ').split())
if (n1 >= n2 and n1 >= n3):
    print('{} é o maior número '.format(n1), end='')
elif (n2 >= n3):
    print('{} é o maior número '.format(n2), end='')
else:
    print('{} é o maior número '.format(n3), end='')
print('e ', end='')
if (n1 <= n2 and n1 <= n3):
    print('{} é o menor número'.format(n1))
elif (n2 <= n3):
    print('{} é o menor número'.format(n2))
else:
    print('{} é o menor número'.format(n3))