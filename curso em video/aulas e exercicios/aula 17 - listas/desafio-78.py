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

quant_maior = lista.count(maior)
quant_menor = lista.count(menor)

print(f'Valores digitados: {lista}')

if (quant_maior == 1):
    print(f'Maior valor: {maior}\nPosição: {lista.index(maior) + 1}', end='')
else:
    print(f'Maior valor: {maior}\nPosições: ', end='')
    indice = 0
    for i in range(0, quant_maior):
        print(f'{lista.index(maior, indice) + 1}', end=' ')
        indice = lista.index(maior, indice) + 1

if (quant_menor == 1):
    print(f'\nMenor valor: {menor}\nPosição: {lista.index(menor) + 1}')
else:
    print(f'\nMenor valor: {menor}\nPosições: ', end='')
    indice = 0
    for i in range(0, quant_menor):
        print(f'{lista.index(menor, indice) + 1}', end=' ')
        indice = lista.index(menor, indice) + 1