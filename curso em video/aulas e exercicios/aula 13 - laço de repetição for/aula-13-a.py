# for -> laço de repetição/iteração com variável de controle
# repete uma instrução a partir de um range definido
# for variavel in range(x, y):
#     instrução
# o ultimo valor do range não é considerado no laço, por ex:
# range(0, 6) -> 0 a 5 range(1, 6) -> 1 a 5
# range(6, 0, -1) -> subtrai 1 em cada laço até chegar em 1(ultimo antes de 0)
# range(0, 10, 2) 0> soma 2 em cada laço, até 9(ultimo antes do 10)

for i in range(10, 0, -1):
  print(i)
for a in range(10, 1, -1):
    print(a)
for b in range(0, 11):
    if (b % 2 == 0):
        print('\033[1;33m{}\033[0;37m'.format(b))
    else:
        print('\033[1;34m{}\033[0;37m'.format(b))