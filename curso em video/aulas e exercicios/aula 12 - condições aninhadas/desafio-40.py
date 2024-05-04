n1 = float(input('\033[1mDigite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if (media >= 7):
    print('\033[1;32mParabéns! Você foi aprovado com média {:.2f}\033[0;37m'.format(media))
elif (media >= 5 and media <= 6.9):
    print('\033[1;33mVocê está de recuperação! Sua média foi {:.2f}\033[0;37m'.format(media))
else:
    print('\033[1;31mVocê está reprovado! Sua média foi {:.2f}\033[0;37m'.format(media))