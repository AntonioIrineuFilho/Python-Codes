# sintaxe -> tupla = (dado, dado, dado, ...)
# receber uma tupla de entrada -> tuple(map(tipo de dado, input().split()))
# as tuplas são imutáveis, ou seja, não é possível modificar ou substituir elementos
# dado = (0, 1, 2, 3, 4, 5)
# dado [0] = 999
# print(dado[0]) -> erro, pois não é possivel alterar um dado em uma tupla

lanche = ('Hamburguer', 'Refrigerante', 'Suco', 'Pizza')

# for i in lanche:
#    if (i == lanche[len(lanche)-1]):
#        print(f'{i}', end='')
#    else:
#        print(f'{i}, ', end='')

# No primeiro caso o i é um elemento da tupla, enquanto no segundo, é o indice

for i in range(len(lanche)):
    if (i == len(lanche) - 1):
        print(f'{lanche[i]}', end='')
    else:
        print(f'{lanche[i]}, ', end='')
