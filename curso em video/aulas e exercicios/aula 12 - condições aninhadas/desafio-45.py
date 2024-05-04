import random

print('-\033[1;37m' * 23)
print('\033[1;32mPedra, \033[1;36mPapel, \033[1;35mTesoura!')
print('\033[1;37m-' * 23)
print('\033[1;32m1-Pedra\n\033[1;36m2-Papel\n\033[1;35m3-Tesoura')
player = int(input('\033[1;37mQual a sua jogada? '))

pc = random.randint(1, 3)

if (player == 1 and pc == 1):
    print('\033[1;33mEmpate! Eu também escolhi pedra!\033[0;37m')
elif (player == 2 and pc == 2):
    print('\033[1;33mEmpate! Eu também escolhi papel!\033[0;37m')
elif (player == 3 and pc == 3):
    print('\033[1;33mEmpate! Eu também escolhi tesoura!\033[0;37m')
elif (player == 1 and pc == 2):
    print('\033[1;31mEu venci! Você escolheu pedra e eu papel!\033[0;37m')
elif (player == 2 and pc == 3):
    print('\033[1;31mEu venci! Você escolheu papel e eu tesoura!\033[0;37m')
elif (player == 3 and pc == 1):
    print('\033[1;31mEu venci! Você escolheu tesoura e eu pedra!\033[0;37m')
elif (player == 1 and pc == 3):
    print('\033[1;34mVocê venceu! Eu escolhi tesoura!\033[0;37m')
elif (player == 2 and pc == 1):
    print('\033[1;34mVocê venceu! Eu escolhi pedra!\033[0;37m')
elif (player == 3 and pc == 2):
    print('\033[1;34mVocê venceu! Eu escolhi papel!\033[0;37m')
else:
    print('\033[1;31mOpção inválida!\033[0;37m')



