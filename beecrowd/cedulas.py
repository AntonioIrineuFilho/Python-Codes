n = int(input())
n_copy = n
cedulas = [100, 50, 20, 10, 5, 2, 1]
notas = []

for i in range(len(cedulas)):
    notas.append(n // cedulas[i])
    n = n % cedulas[i]

print(n_copy)
for i in range(len(cedulas)):
    print(f'{notas[i]} nota(s) de R$ {cedulas[i]},00')
