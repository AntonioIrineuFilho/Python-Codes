lista = []
lista_vanilla = []
lista_desc = []
cont = 0

while True:
    while True:
        n = int(input(f'Digite o {cont+1}º número inteiro: '))
        lista.append(n)
        lista_vanilla.append(n)
        cont = cont + 1
        if (cont % 5 == 0):
            break
    op = int(input('Digite 1 para adicionar mais valores ou 0 para continuar: '))
    while True:
        if (op == 1 or op == 0):
            break
        else:
            op = int(input('Opção inválida. Por favor, digite 1 ou 0: '))
    if (op == 0):
        break

while True:
    maior = 0
    for i in range(len(lista)):
        if (lista[i] >= lista[maior]):
            maior = i
    lista_desc.append(lista[maior])
    del(lista[maior])
    if (len(lista) == 0):
        break

print(f'Foram digitados {len(lista_vanilla)} valores')
print(f'Lista(Ordem Digitada): {lista_vanilla}')
print(f'Lista(Ordem Crescente): {sorted(lista_vanilla)}')
print(f'Lista(Ordem Decrescente): {lista_desc}')