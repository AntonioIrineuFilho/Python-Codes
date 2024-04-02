print('------------------Calculadora de dois números------------------')
n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
print('{} + {} = {}\n{} - {} = {}'.format(n1, n2, soma, n1, n2, sub))
print('{} x {} = {}'.format(n1, n2, mult))
if (n1 % n2 == 0):
    print('{} / {} = {}'.format(n1, n2, int(div)))
else:
    print('{} / {} = {:.2f}'.format(n1, n2, div))