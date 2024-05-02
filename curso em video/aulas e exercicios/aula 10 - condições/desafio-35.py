a, b, c = map(int, input('Digite o comprimento das três retas: ').split())
if (a + b > c and a + c > b and b + c > a):
    print('É possível formar um triângulo com as três retas dadas')
else:
    print('Não é possível formar um triângulo com as três retas dadas')