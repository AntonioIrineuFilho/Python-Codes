preco = float(input('\033[1;37mInforme o preço do produto: '))
print('Formas de Pagamento:')
print('\033[1;32m1-À vista dinheiro/cheque')
print('\033[1;33m2-À vista no cartão')
print('\033[1;34m3-2x no cartão')
print('\033[1;35m4-3x ou mais no cartão')
cond = int(input('\033[1;37mInforme o número da forma desejada: '))
if (cond == 1):
    print('\033[1;32mO preço final do produto à vista no dinheiro/cheque será R${:.2f}\033[0;37m'.format(preco - preco * 0.1))
elif (cond == 2):
    print('\033[1;33mO preço final do produto à vista no cartão será R${:.2f}\033[0;37m'.format(preco - preco * 0.05))
elif (cond == 3):
    print('\033[1;34mO preço final do produto em 2x no cartão será R${:.2f}\033[0;37m'.format(preco))
elif (cond == 4):
    print('\033[1;35mO preço final do produto em 3x ou mais no cartão será R${:.2f}\033[0;37m'.format(preco + preco * 0.2))
else:
    print('\033[1;31mOpção inválida\033[0;37m')   
