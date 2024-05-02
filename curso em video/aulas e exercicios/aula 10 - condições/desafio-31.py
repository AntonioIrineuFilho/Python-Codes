print('----------Preço da Passagem----------')
km = float(input('Digite a distância da viagem: '))
if (km <= 200):
    print('O preço da passagem para uma viagem de {:.2f} km é de R$ {:.2f}'.format(km, 0.5 * km))
else:
    print('O preço da passagem para uma viagem de {:.2f} km é de R$ {:.2f}'.format(km, 0.45 * km))