n = int(input())
cedulas = [100, 50, 20, 10, 5, 2, 1]
notas = []

for i in range(len(cedulas)):
    notas.append(n // cedulas[i])
    n = n % cedulas[i]

print(notas)
