n = 0
q = 0
s = 0
x = 0

while x != 999:
    if (x == 0):
        while x != 5:
            n = int(input('Digite um valor: '))
            q = q + 1
            s = s + n
            x = x + 1
        x = int(input('Digite 0 para continuar e 999 para parar: '))
    else:
        x = int(input('Opção inválida! Por favor, digite 0 se quiser continuar ou 999 se quiser parar: '))


print('Foram digitados {} valores'.format(q))
print('A soma dos valores digitados é {}'.format(s))

