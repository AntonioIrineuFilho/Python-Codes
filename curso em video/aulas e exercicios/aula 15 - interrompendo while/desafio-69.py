m18 = 0
masc = 0
fem20 = 0

while True:
    sexo = input('Digite o sexo[M/F]: ').strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Digite o sexo[M/F]: ').strip().upper()
    idade = int(input('Digite a idade: '))
    if (idade > 18):
        m18 = m18 + 1
    if (sexo == 'M'):
        masc = masc + 1
    if (sexo == 'F' and idade < 20):
        fem20 = fem20 + 1
    x = int(input('Digite 1 para continuar ou 0 para encerrar: '))
    while x != 1 and x != 0:
        x = int(input('Digite 1 para continuar ou 0 para encerrar: '))
    if (x == 0):
        break

print(f'Foram cadastradas {m18} pessoas maiores de 18 anos')
print(f'Foram cadastrados {masc} homens')
print(f'Foram cadastradas {fem20} mulheres com menos de 20 anos')


