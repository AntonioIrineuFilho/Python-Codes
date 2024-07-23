cont = 0
lista = []
lista_pares = []
lista_impares = []

while True:
    while True:
        n = int(input(f'Digite o {cont+1} número: '))
        lista.append(n)
        cont = cont + 1
        if (cont % 5 == 0):
            break
    op = int(input('Digite 1 para adicionar mais valores ou 0 para continuar: '))
    while True:
        if (op == 1 or op == 0):
            break
        else:
            op = int(input('Opção inválida. Digite 1 para adicionar mais valores ou 0 para continuar: '))
    if (op == 0):
        break

for i in lista:
    if (i % 2 == 0):
        lista_pares.append(i)
    else:
        lista_impares.append(i)

print(f'Lista Completa: {lista}')
print(f'Lista dos Pares: {lista_pares}')
print(f'Lista dos Impares: {lista_impares}')