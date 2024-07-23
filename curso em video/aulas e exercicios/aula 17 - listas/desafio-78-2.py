lista = []
cont = 0
opv = [0, 1]
maior = 0
menor = 999999999999999999999

while True:
    while True:
        li = int(input(f'Digite um valor para a posição {cont+1}: '))
        lista.append(li)
        cont = cont + 1
        if (cont % 3 == 0):
            break
    op = int(input('Digite 1 para adicionar mais valores ou 0 para continuar: '))
    while True:
        if (op in opv):
            break
        else:
            op = int(input('Opção inválida. Por favor, digite 1 ou 0: '))
    if (op == 0):
        break

for i in lista:
    if (i >= maior):
        maior = i
    if (i <= menor):
        menor = i

print(f'Lista: {lista}')

if (lista.count(maior) == 1):
    print(f'Maior: {maior}\nPosição: {lista.index(maior) + 1}', end='')
else:
    print(f'Maior: {maior}\nPosições: ', end='')
    for i in range(len(lista)):
        if (lista[i] == maior):
            print(f'{i+1}', end=' ')

if (lista.count(menor) == 1):
    print(f'\nMenor: {menor}\nPosição: {lista.index(menor) + 1}', end='')
else:
    print(f'\nMenor: {menor}\nPosições: ', end='')
    for i in range(len(lista)):
        if (lista[i] == menor):
            print(f'{i+1}', end=' ')
    