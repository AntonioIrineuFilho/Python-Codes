dias = int(input('Quantos dias você alugou? '))
km = float(input('Quantos km foram rodados? '))
pg = dias * 60 + km * 0.15
if (int(pg) == pg):
    print('O custo do aluguel do carro foi de R$ {}'.format(int(pg)))
else:
    print('O custo do aluguel do carro foi de R$ {:.2f}'.format(pg))