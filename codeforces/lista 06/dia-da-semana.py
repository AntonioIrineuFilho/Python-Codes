def dia_da_semana(h, d):
    week = ['Domingo', 'Segunda-feira', 'Terca-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado']
    indice = week.index(h)
    dia = (indice + d) % 7
    return week[dia]

h = input('Hoje: ')
d = int(input('Quantos dias faltam: '))

print(dia_da_semana(h, d))