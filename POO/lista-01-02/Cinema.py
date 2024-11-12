class Entrada:
    def __init__(self):
        self.dia = int()
        self.hora = float()

    def Inteira(self):
        if (self.dia == 2 or self.dia == 3 or self.dia == 5):
            if (self.hora >= 17 or self.hora == 0):
                inteira = 16 + 16 * 0.5
            else:
                inteira = 16
        elif (self.dia == 4):
            inteira = 8
        else:
            if (self.hora >= 17 or self.hora == 0):
                inteira = 20 + 20 * 0.5
            else:
                inteira = 20
        return inteira

    def Meia(self):
        if (self.dia == 2 or self.dia == 3 or self.dia == 5):
            if (self.hora >= 17 or self.hora == 0):
                meia = (16 + 16 * 0.5) / 2
            else:
                meia = 16 / 2
        elif (self.dia == 4):
            meia = 8
        else:
            if (self.hora >= 17 or self.hora == 0):
                meia = (20 + 20 * 0.5) / 2
            else:
                meia = 20 / 2
        return meia
    
print('1-Domingo\n2-Segunda-feira\n3-Terça-feira\n4-Quarta-feira\n5-Quinta-feira\n6-Sexta-feira\n7-Sábado')
d = int(input('Digite o dia da sessão desejada: '))
while True:
    if (d >= 1 and d <= 7):
        break
    else:
        d = int(input('Dia inválido. Digite o dia da sessão desejada: '))
h = float(input('Digite a hora da sessão desejada: '))
entrada1 = Entrada()
entrada1.dia = d
entrada1.hora = h
print('1-Entrada Inteira\n2- Meia Entrada')
op = int(input('Digite a opção da informação desejada: '))
while True:
    if (op == 1 or op == 2):
        break
    else:
        op = int(input('Opção inválida. Digite a opção da informação desejada: '))
if (op == 1):
    print(f'Valor da entrada inteira: R$ {entrada1.Inteira():.2f}')
else:
    print(f'Valor da entrada meia: R$ {entrada1.Meia():.2f}')
