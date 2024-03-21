M = int(input())
A = int(input())
B = int(input())
C = M - (A + B)
if (A > B and A > C):
    print(A)
elif (B > A and B > C):
    print(B)
else:
    print(C)