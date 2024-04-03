A = int(input())
B = int(input())
C = int(input())
D = int(input())
d1 = (A + B) - (C + D)
d2 = (A + C) - (B + D)
d3 = (A + D) - (B + C)
d4 = (C + D) - (A + B)
d5 = (B + D) - (A + C)
d6 = (B + C) - (A + D)
if (d1 == 0 or d2 == 0 or d3 == 0 or d4 == 0 or d5 == 0 or d6 == 0):
    print("0")
elif (d1 > 0 and d2 > 0 and d3 > 0):
    if (d1 <= d2 and d1 <= d3):
        print(d1)
    elif (d2 <= d3):
        print(d2)
    else:
        print(d3)
elif (d1 > 0 and d2 > 0 and d6 > 0):
    if (d1 <= d2 and d1 <= d6):
        print(d1)
    elif (d2 <= d6):
        print(d2)
    else:
        print(d6)
elif (d1 > 0 and d3 > 0 and d5 > 0):
    if (d1 <= d3 and d1 <= d5):
        print(d1)
    elif (d3 <= d5):
        print(d3)
    else:
        print(d5)
elif (d1 > 0 and d5 > 0 and d6 > 0):
    if (d1 <= d5 and d1 <= d6):
        print(d1)
    elif (d5 <= d6):
        print(d5)
    else:
        print(d6)
elif (d2 > 0 and d3 > 0 and d4 > 0):
    if (d2 <= d3 and d2 <= d4):
        print(d2)
    elif (d3 <= d4):
        print(d3)
    else:
        print(d4)
elif (d2 > 0 and d4 > 0 and d6 > 0):
    if (d2 <= d4 and d2 <= d6):
        print(d2)
    elif (d4 <= d6):
        print(d4)
    else:
        print(d6)
elif (d3 > 0 and d4 > 0 and d5 > 0):
    if (d3 <= d4 and d3 <= d5):
        print(d3)
    elif (d4 <= d5):
        print(d4)
    else:
        print(d5)
elif (d4 > 0 and d5 > 0 and d6 > 0):
    if (d4 <= d5 and d4 <= d6):
        print(d4)
    elif (d5 <= d6):
        print(d5)
    else:
        print(d6)



