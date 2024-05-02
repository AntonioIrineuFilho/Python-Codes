print('----------Calculadora de Ano Bissexto----------')
ano = int(input('Digite um ano: '))
ano2 = str(ano)
if (ano % 4 == 0 and ano2[2:] != '00'):
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))