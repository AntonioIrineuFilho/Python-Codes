# li = list(map(int, input('Digite seis números: ').split()))
# s = 0          
# for i in range(len(li)):
#    if (li[i] % 2 == 0):
#        s = s + li[i]
# print('A soma dos números pares digitados é {}'.format(s))
s = 0
for i in range (0, 6):
    n = int(input('Digite um número: '))
    if (n % 2 == 0):
        s = s + n
print(s)
print('FIM')