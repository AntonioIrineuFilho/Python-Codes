A1 = int(input())
A2 = int(input())
A3 = int(input())
T1 = (A2 * 2) + (A3 * 4)
T2 = (A1 * 2) + (A3 * 2)
T3 = (A2 * 2) + (A1 * 4)
if (T1 <= T2 and T1 <= T3):
    print(T1)
elif (T2 <= T3):
    print(T2)
else:
    print(T3)