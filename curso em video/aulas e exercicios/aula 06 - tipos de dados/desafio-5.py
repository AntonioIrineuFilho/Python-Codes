x = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(x))
print('Só tem espaços?', x.isspace())
print('É um número?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('É alfanumérico?', x.isalnum())
print('Está em maiusculas?', x.isupper())
print('Está em minusculas?', x.islower())
print('Está capitalizado?', x.istitle())