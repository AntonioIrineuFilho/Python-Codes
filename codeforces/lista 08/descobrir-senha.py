casos = []
while True:
    try:
        while True:
            n = int(input())
            if (n == 0):
                break
            teclas = list(map(float, input().split()))
            digitos = []
            x = sorted(teclas)
            for i in range(0, n):
                if (x[len(teclas)-(i+1)] in digitos):
                    indice = teclas.index(x[len(teclas)-(i+1)], indice+1)
                    digitos.append(indice)
                    digitos.append(x[len(teclas)-(i+1)])
                else:
                    indice = teclas.index(x[len(teclas)-(i+1)])
                    digitos.append(indice)
                    digitos.append(x[len(teclas)-(i+1)])
            senha = ''
            for j in range(0, len(digitos), 2):
                senha = senha + str(digitos[j])
            casos.append(senha)
    except EOFError:
        break

for k in range(len(casos)):
    print(f'Caso {k+1}: {casos[k]}')