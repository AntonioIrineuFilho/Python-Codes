def dia_da_semana(h, d):
    week = ['Domingo', 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado']
    dia = d % 7
    indice = week.index(h)
    return week[indice+dia]

h = input('Hoje: ')
d = int(input('Quantos dias faltam: '))

print(dia_da_semana(h, d))