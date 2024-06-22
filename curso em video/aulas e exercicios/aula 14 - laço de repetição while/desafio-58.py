import random

print('Eu pensei em um número de 1 a 10. Tente advinhar!')
pc = random.randint(1, 10)
pl = int(input('Qual seu palpite? '))
t = 1
while pc != pl:
    pl = int(input('Errou! Vamos lá, dê outro palpite: '))
    t = t + 1

if (t == 1):
    print('Uau! Você acertou de primeira!')
    print('Isso mesmo! Eu pensei no número {}!'.format(pc))
else:
    print('Isso mesmo! Eu pensei no número {}!'.format(pc))
    print('Você acertou em {} tentativas!'.format(t))
