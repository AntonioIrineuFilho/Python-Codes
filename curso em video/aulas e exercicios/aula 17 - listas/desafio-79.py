lista = []
cont = 0
opv = [0, 1]

while True:
    while True:
        n = int(input('Digite um número: '))
        if (n not in lista):
            lista.append(n)
        cont = cont + 1
        if (cont % 5 == 0):
            break
    op = int(input('Digite 1 para adicionar mais valores ou 0 para continuar: '))
    while True:
        if (op in opv):
            break
        else:
            op = int(input('Opção inválida. Por favor, digite 1 ou 0: '))
    if (op == 0):
        break

print(f'A lista digitada de forma única e ordenada é: {sorted(lista)}')

        
