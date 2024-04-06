import math
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('A média arredondada é {}'.format(math.ceil((n1+n2)/2)))
print('A média truncada é {}'.format(math.trunc((n1+n2)/2)))