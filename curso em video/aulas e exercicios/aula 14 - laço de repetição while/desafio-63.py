print('-'*23)
print('Sequência de Fibonacci')
print('-'*23)

n = int(input('Digite quantos termos você deseja: '))

t1 = 0
t2 = 1
x = 2

if (n == 1):
    print(t1)
    print('-FIM-')
elif (n == 2):
    print('{} -> {}'.format(t1, t2), end='')
    print('-FIM-')
elif (n > 2):
    print('{} -> {}'.format(t1, t2), end='')
    while x != n:
        t3 = t1 + t2
        print(' -> {}'.format(t3), end='')
        t1 = t2
        t2 = t3
        x = x + 1
    print('\n-FIM-')
else:
    print('-FIM-')

    