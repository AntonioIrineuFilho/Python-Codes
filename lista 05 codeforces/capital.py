A1, A2, A3, A4 = map(int, input().split())
L1 = A1 ** (1/2)
L4 = A4 ** (1/2)
if (L1 * L4 == A2 and L1 * L4 == A3):
    print("S")
else:
    print("N")