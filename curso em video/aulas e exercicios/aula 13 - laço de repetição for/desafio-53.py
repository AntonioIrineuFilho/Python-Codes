x = input('Digite uma frase: ').upper().split()
y = ''.join(x)
li = []
for i in range(len(y)):
    if (y[i] == y[len(y)-(i+1)]):
        li.append(y[i])
if (len(li) == len(y)):
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')