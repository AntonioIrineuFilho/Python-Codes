# x = input('Digite uma frase: ').upper().split()
# y = ''.join(x)
# li = []
# for i in range(len(y)):
#    if (y[i] == y[len(y)-(i+1)]):
#        li.append(y[i])
# if (len(li) == len(y)):
#    print('A frase digitada é um palíndromo')
# else:
#   print('A frase digitada não é um palíndromo')

x = input('Digite uma frase: ').strip().upper().split()
y = ''.join(x)
s = 0

if ((len(y) + 1) % 2 == 0):
    for i in range(0, (len(y)-1)//2):
        if (y[i] == y[len(y)-(i+1)]):
            s = s + 1
else:
    for i in range(0, len(y)//2):
        if (y[i] == y[len(y)-(i+1)]):
            s = s + 1

if (s == (len(y)-1)/2 or s == len(y)/2):
    print('A frase digitada é um palindromo')
else:
    print('A frase digitada não é um palindromo')