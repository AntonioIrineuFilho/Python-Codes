A1, A2, A3, A4 = map(int, input().split())
if (A1 * A4 == A2 * A3 or A1 * A3 == A2 * A4 or A1 * A2 == A3 * A4):
    print("S")
else:
    print("N")