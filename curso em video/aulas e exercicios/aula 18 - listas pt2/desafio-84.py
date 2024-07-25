lista1 = []
lista2 = []
mais_pesadas = []
mais_leves = []
maior = 0
menor = 99999999999999999999999

while True:
    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))
    lista1.append(nome)
    lista1.append(peso)
    op = int(input('Digite 1 para continuar e 0 para encerrar: '))
    while True:
        if (op == 1 or op == 0):
            break
        else:
            op = int(input('Opção inválida. Digite 1 para continuar e 0 para encerrar: '))
    if (op == 0):
        break

for i in range(0, len(lista1), 2):
    lista2.append(lista1[i:i+2])

for i in range(len(lista2)):
    if (lista2[i][1] >= maior):
        maior = lista2[i][1]
    if (lista2[i][1] <= menor):
        menor = lista2[i][1]

for i in range(len(lista2)):
    if (lista2[i][1] == maior):
        mais_pesadas.append(lista2[i][0])
    if (lista2[i][1] == menor):
        mais_leves.append(lista2[i][0])

print(f'Foram cadastradas {len(lista1)//2} pessoas')
print(f'As pessoas mais leves tiveram o peso de {menor} kilos, e foram: {mais_leves}')
print(f'As pessoas mais pesadas tiveram o peso de {maior} kilos, e foram: {mais_pesadas}')
