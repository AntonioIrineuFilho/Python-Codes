x = input('Digite um número: ')
if (len(x) == 4):
    print('Unidade: {}'.format(x[3]))
    print('Dezena: {}'.format(x[2]))
    print('Centena: {}'.format(x[1]))
    print('Milhar: {}'.format(x[0]))
elif (len(x) == 3):
    print('Unidade: {}'.format(x[2]))
    print('Dezena: {}'.format(x[1]))
    print('Centena: {}'.format(x[0]))
    print('Milhar: 0')
elif (len(x) == 2):
    print('Unidade: {}'.format(x[1]))
    print('Dezena: {}'.format(x[0]))
    print('Centena: 0')
    print('Milhar: 0')
else:
    print('Unidade: {}'.format(x[0]))
    print('Dezena: 0')
    print('Centena: 0')
    print('Milhar: 0')