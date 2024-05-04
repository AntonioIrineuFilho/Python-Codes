import datetime
from datetime import timedelta, datetime

data_atual = datetime.now()

data_nasc = input('\033[1;37mDigite sua data de nascimento: ')
data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y")

dif = data_atual - data_nasc
idade = timedelta.total_seconds(dif) // 31536000

if (idade <= 9):
    print('\033[1;37mSua categoria é \033[1;31mMIRIM\033[0;37m')
elif (idade <= 14):
    print('\033[1;37mSua categoria é \033[1;32mINFANTIL\033[0;37m')
elif (idade <= 19):
    print('\033[1;37mSua categoria é \033[1;33mJUNIOR\033[0;37m')
elif (idade == 20):
    print('\033[1;37mSua categoria é \033[1;34mSENIOR\033[0;37m')
else:
    print('\033[1;37mSua categoria é \033[1;35mMASTER\033[0;37m')
