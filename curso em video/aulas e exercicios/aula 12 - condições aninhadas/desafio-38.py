n1 = int(input('\033[1mDigite um número: '))
n2 = int(input('Digite outro número: '))
if (n1 > n2):
    print('\033[1;32m{} \033[1;37mé maior que \033[1;31m{}\033[0;37m'.format(n1, n2))
elif (n1 == n2):
    print('\033[1;33m{} \033[1;37mé igual a \033[1;33m{}\033[0;37m'.format(n1, n2))
else:
    print('\033[1;32m{} \033[1;37mé maior que \033[1;31m{}\033[0;37m'.format(n2, n1))