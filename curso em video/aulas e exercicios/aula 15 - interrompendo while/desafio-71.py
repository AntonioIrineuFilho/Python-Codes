n = int(input('Digite o valor do saque: '))
cont = 50

while True:
    notas = n // cont
    n = n % cont
    print(f'Notas de {cont}: {notas}')
    if (cont == 50):
        cont = 20
    elif (cont == 20):
        cont = 10
    elif (cont == 10):
        cont = 1
    else:
        break

    