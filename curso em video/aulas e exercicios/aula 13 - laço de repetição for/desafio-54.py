# x = 0
# y = 0
# for i in range (0, 7):
#    n = int(input('Digite uma idade: '))
#   if (n < 21):
#       x = x + 1
#    else:
#        y = y + 1
# print('Existem {} menores de idade e {} maiores de idade'.format(x, y))

menor = 0
maior = 0

for i in range(0, 6):
    y, m, d = map(int, input('Digite o ano, o mês e o dia de nascimento: ').split())
    nasc = (y*365) + (m*30) + d
    data_atual = (2024*365) + (5*30) + 25
    if ((data_atual - nasc) / 365 < 21):
        menor = menor + 1
    else:
        maior = maior + 1

print('{} são de menor e {} são de maior'.format(menor, maior))
