print('--------Calculadora de Multa--------')
vm = float(input('Digite a velocidade que você está dirigindo: '))
if (vm > 80):
    print('Você foi multado em R$ {:.2f}'.format((vm - 80) * 7))
else:
    print('Você não foi multado')