x = int(input('Digite um número: '))
uni = x % 10
x = x // 10
dez = x % 10
x = x // 10
cen = x % 10
x = x // 10
mil = x % 10
print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cen))
print('Milhar: {}'.format(mil))