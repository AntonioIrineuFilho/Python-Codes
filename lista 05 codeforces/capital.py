A1, A2, A3, A4 = map(int, input().split())
# Se a proporção A1/A2 = A3/A4(ou qualquer proporção entre essas variáveis) for igual, significa que é possível formar angulos reto, uma vez que a inclinação do angulo reto é igual a 1
# A1/A2 = A3/A4 -> A1 * A4 = A2 * A3
if (A1 * A4 == A2 * A3 or A1 * A3 == A2 * A4 or A1 * A2 == A3 * A4):
    print("S")
else:
    print("N")