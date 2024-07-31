A, B, C = map(int, input().split())
if (A == B or A == C or B == C):
    print("S")
elif (A + B - C == 0 or A + C - B == 0 or B + C - A == 0):
    print("S")
elif (A - B + C == 0 or A - C + B == 0 or B - C + A == 0 or B - A + C == 0 or C - A + B == 0 or C - B + A == 0):
    print("S")
else:
    print("N")