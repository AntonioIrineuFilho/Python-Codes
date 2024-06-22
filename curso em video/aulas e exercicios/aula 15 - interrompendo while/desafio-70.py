s = 0
q = 0
menor = 999999999999

while True:
    nome = input('Digite o nome do produto: ').strip().upper()
    preco = float(input('Digite o preço do produto: '))
    s = s + preco
    if (preco > 1000):
        q = q + 1
    if (preco <= menor):
        menor = preco
        mb = nome
    x = int(input('Digite 1 para continuar ou 0 para encerrar: '))
    while x != 1 and x != 0:
        x = int(input('Digite 1 para continuar ou 0 para encerrar: '))
    if (x == 0):
        break

print(f'O preço total dos produtos digitados é R${s:.2f}')
print(f'{q} produtos custam mais de R$1.000,00')
print(f'O produto mais barato é o {mb} e custa R${menor:.2f}')

    
