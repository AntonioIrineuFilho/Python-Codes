# break -> interrompe o while e segue o código
# while True -> while infinito, só para com o break

cont = 1

# while cont <= 10:
#    print(cont)
#    cont = cont + 1

while True:
    print(f'O contador está em {cont}')
    cont = cont + 1
    if (cont > 10):
        break