import random

print("""----------Brincadeira da Advinhação----------
A bricandeira é a seguinte: eu vou pensar em um número inteiro de 0 a 5 e você deve tentar adivinhar qual é!""")
n = int(input('E aí, qual é seu palpite? '))
x = random.randint(0, 5)
if (n == x):
    print('Parabéns, você acertou! O número que eu pensei foi {}'.format(x))
else:
    print('Que pena, você errou! O número que eu pensei foi {}'.format(x))