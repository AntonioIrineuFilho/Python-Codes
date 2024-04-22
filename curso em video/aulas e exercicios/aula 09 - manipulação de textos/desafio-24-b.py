x = input('Digite o nome de uma cidade: ')
li_x = x.split()
if (li_x[0].upper() == 'SANTO'):
    print('A cidade {} começa com a palavra "SANTO"'.format(x))
else:
    print('A cidade {} não começa com a palavra "SANTO"'.format(x))