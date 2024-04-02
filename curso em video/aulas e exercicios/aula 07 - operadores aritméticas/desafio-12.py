b = float(input('Digite a largura da parede em metros: '))
h = float(input('Digite a altura da parede em metros: '))
area = b*h
print('A área da parede é {:.2f} metros quadrados'.format(area))
print('Serão precisos {:.2f} litros de tinta para pintar toda a parede'.format(area/2))
