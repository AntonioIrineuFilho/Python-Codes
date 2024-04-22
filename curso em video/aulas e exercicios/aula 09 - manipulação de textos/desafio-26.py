x = input('Digite uma frase: ')
if (x.upper().count('A') == 0):
    print('A frase não possui letras "A"')
else:
    if (x.upper().count('A') == 1):
        print('A letra "A" aparece {} vez na frase'.format(x.upper().count('A')))
        print('A letra "A" aparece pela primeira vez na posição {} da frase'.format(x.upper().strip().find('A')))
        for i in range(len(x.strip())):
            if (x[i].upper() == 'A'):
                y = i
        print('A letra "A" aparece pela última vez na posição {} da frase'.format(y))
    else:
        print('A letra "A" aparece {} vezes na frase'.format(x.upper().count('A')))
        print('A letra "A" aparece pela primeira vez na posição {} da frase'.format(x.upper().strip().find('A')))
        for i in range(len(x.strip())):
            if (x[i].upper() == 'A'):
                y = i
        print('A letra "A" aparece pela última vez na posição {} da frase'.format(y))