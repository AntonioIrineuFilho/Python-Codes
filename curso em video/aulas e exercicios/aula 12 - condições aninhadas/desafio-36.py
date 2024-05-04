print('\033[1;33m-' * 25)
print('Aprovação de Empréstimo')
print('-' * 25)

casa = float(input('\033[1;37mDigite o valor da casa: '))
sal = float(input('Digite seu salário: '))
anos = float(input('Digite em quantos anos você pretende pagar: '))
prest = casa / (anos * 12)

if (prest > sal * 0.3):
    print('\033[1;31mNão será possível realizar o empréstimo\033[1m, pois as prestações mensais ficariam R$ {:.2f},'.format(prest)) 
    print('o que representa {:.2f} % do seu salário\033[m'.format((prest * 100) / sal))
else:
    print('\033[1;32mSerá possível realizar o empréstimo, pois as prestações mensais ficarão R$ {:.2f},'.format(prest))
    print('o que representa {:.2f} % do seu salário\033[m'.format((prest * 100) / sal))