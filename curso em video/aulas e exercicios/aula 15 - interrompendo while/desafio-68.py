import random

pc = random.randint(0, 10)
cont = 0

while True:
    pl = int(input('Escolha um número(0-10): '))
    x = input('Digite P para par e I para ímpar: ').strip().upper()
    s = pl + pc
    if (x == 'P' and s % 2 == 0):
        print(f'Você ganhou! Eu escolhi {pc} e você escolheu {pl}, resultando no número par {s}')
    elif (x == 'I' and not s % 2 == 0):
        print(f'Você ganhou! Eu escolhi {pc} e você escolheu {pl}, resultando no número ímpar {s}')
    elif (x == 'P' and not s % 2 == 0):
        print(f'Você perdeu! Eu escolhi {pc} e você escolheu {pl}, resultando no número ímpar {s}')
        print(f'Você ganhou {cont} vezes consecutivas!')
        break
    else:
        print(f'Você perdeu! Eu escolhi {pc} e você escolheu {pl}, resultando no número par {s}')
        print(f'Você ganhou {cont} vezes consecutivas!')
        break
    cont = cont + 1

        
