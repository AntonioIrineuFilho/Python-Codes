def dia(dia, mes, ano):
    meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    dpm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (dia <= 0 or dia > 31):
        return 'Data Invalida'
    elif (mes <= 0 or mes > 12):
        return 'Data Invalida'
    for i in range(0, 12):
        if (mes-1 == i):
            mes = meses[i]
            dmax = dpm[i]
            break
    if (dia > dmax):
        return 'Data Invalida'
    else:
        return f'{dia:02d} de {mes} de {ano}'
    

entrada = input('Digite a data(dd/mm/aaaa): ').strip()
d = int(entrada[:2])
m = int(entrada[3:5])
a = int(entrada[6:])

print(dia(d, m, a))