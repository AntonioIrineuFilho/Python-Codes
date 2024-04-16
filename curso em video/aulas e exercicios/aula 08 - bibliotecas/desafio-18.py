import math

x = float(input('Digite o valor do ângulo: '))
rad = (math.pi * x) / 180
if (math.sin(rad) == 0.9999999999999999):
    print('Seno: 1')
else:
    print('Seno: {:.2f}'.format(math.sin(rad)))
if (math.cos(rad) == 0.9999999999999999):
    print('Cosseno: 1')
else:
    print('Cosseno: {:.2f}'.format(math.cos(rad)))
if (math.tan(rad) == 0.9999999999999999):
    print('Tangente: 1')
else:
    print('Tangente: {:.2f}'.format(math.tan(rad)))
