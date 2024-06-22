n = 0
s = 0
q = 0
x = 'S'
maior = 0
menor = 99999999999999

while x == 'S':
    cont = 0
    while cont != 5:
        n = int(input('Digite um valor: '))
        if (n >= maior):
            maior = n
        if (n <= menor):
            menor = n
        s = s + n
        q = q + 1
        cont = cont + 1
    x = input('Deseja continuar?[S/N] ').strip().upper()

print('A média dos valores digitados é {:.1f}'.format(s/q))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))



