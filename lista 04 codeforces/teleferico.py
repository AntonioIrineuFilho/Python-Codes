C = int(input())
A = int(input())
if (C > A):
    print("1")
elif (C == A):
    print("2")
elif (A % (C - 1) != 0):
    V = (A // (C - 1)) + 1
    print(V)
else:
    V = (A // (C - 1))
    print(V)
