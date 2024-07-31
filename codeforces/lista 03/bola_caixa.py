# N = diametro da bola
# A, L, P = altura, largura e profundidade
N = float(input())
A, L, P = map(float, input().split())
if (N <= A and N <= L and N <= P):
    print("S")
else:
    print("N")

