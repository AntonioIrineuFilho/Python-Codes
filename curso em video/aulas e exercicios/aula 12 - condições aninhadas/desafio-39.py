import datetime
from datetime import date, timedelta

y = date.today().year
m = date.today().month
d = date.today().day

ano = int(input('Informe o ano que você nasceu: '))
mes = int(input('Informe o número do mês que você nasceu: '))
dia = int(input('Informe o dia que você nasceu: '))

dif = datetime.datetime(y, m, d, 0, 0) - datetime.datetime(ano, mes, dia, 0, 0)
idade = timedelta.total_seconds(dif)//31536000

if (idade == 18):
    print('Você deve se alistar o quanto antes! Já está na hora!')
elif (idade > 18):
    print('Você perdeu o prazo! Você já devia ter se alistado há {} anos!'.format(int(idade-18)))
else:
    print('Você deve se alistar em {} anos!'.format(int(18-idade)))
