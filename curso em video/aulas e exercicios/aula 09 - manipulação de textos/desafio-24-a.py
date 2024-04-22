x = input('Digite o nome de uma cidade: ')
li_x = x.split()
print('A cidade {} começa com "SANTO"? {}'.format(x, li_x[0].upper() == 'SANTO'))