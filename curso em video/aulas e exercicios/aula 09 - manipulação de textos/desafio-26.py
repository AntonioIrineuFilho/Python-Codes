x = input('Digite uma frase: ').strip().upper()
if (x.count('A') == 0):
    print('A frase não possui letras "A"')
else:
    if (x.count('A') == 1):
        print('A letra "A" aparece {} vez na frase'.format(x.count('A')))
        print('A letra "A" aparece pela primeira vez na posição {} da frase'.format(x.find('A')))
        for i in range(len(x)):
            if (x[i] == 'A'):
                y = i
        print('A letra "A" aparece pela última vez na posição {} da frase'.format(y))
    else:
        print('A letra "A" aparece {} vezes na frase'.format(x.count('A')))
        print('A letra "A" aparece pela primeira vez na posição {} da frase'.format(x.find('A')))
        for i in range(len(x)):
            if (x[i] == 'A'):
                y = i
        print('A letra "A" aparece pela última vez na posição {} da frase'.format(y))