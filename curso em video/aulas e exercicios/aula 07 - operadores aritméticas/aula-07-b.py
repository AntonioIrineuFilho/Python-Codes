n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
print('O resultado da soma entre {} e {} é {}, da subtração é {}'.format(n1, n2, soma, sub), end = '')
print(', da multiplicação é {} e da divisão é {:.2f}'.format(mult, div))