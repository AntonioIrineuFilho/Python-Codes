ext = 'zero um dois três quatro cinco seis sete oito nove dez onze doze treze quatorze quinze dezesseis dezessete dezoito dezenove vinte'.split()
ext = tuple(ext)
n = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

while True:
    x = int(input('Digite um número(0-20): '))
    while True:
        if (x > 20 or x < 0):
            x = int(input('Valor inválido. Digite um número(0-20): '))
        else:
            break
    for i in range(len(ext)):
        if (n[i] == x):
            print(f'O número escolhido por extenso é {ext[i].upper()}')
            break
    y = int(input('Digite 1 para continuar e 0 para encerrar: '))
    if (y == 0):
        print('-FIM-')
        break