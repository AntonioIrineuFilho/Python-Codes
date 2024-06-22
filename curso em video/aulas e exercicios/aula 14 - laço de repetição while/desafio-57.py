s = input('Digite seu sexo[M/F]: ').upper().strip()

while not s == 'M' and not s == 'F':
    s = input('Resposta inválida. Por favor, digite M se for homem ou F se for mulher: ').upper().strip()


if (s == 'M'):
    print('Então você é um homem!')
else:
    print('Então você é uma mulher!')