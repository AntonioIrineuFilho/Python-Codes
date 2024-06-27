t = ('Lápis', '1.75', 'Borracha', '2.00', 'Caderno', '15.90', 'Estojo', '25.00', 'Transferidor', '4.20', 'Compasso', '9.99', 'Mochila', '120.32', 'Canetas', '22.30', 'Livro', '34.90')

for i in range(len(t)//2):
        print(f'{t[i+i]}'+(17-len(t[i+i]))*'.'+f'R${t[i+i+1].rjust(7)}')