N1, D1, V1 = map(int, input().split())
N2, D2, V2 = map(int, input().split())
T1 = (D1 / 1000) / V1
T2 = (D2 / 1000) / V2
if (T1 < T2):
    print(N1)
else:
    print(N2)
