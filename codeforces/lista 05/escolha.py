a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
if (a2 - a1 <= 0 and b2 - b1 <= 0 and c2 - c1 <= 0):
    print("0")
elif (a2 - a1 <= 0 and b2 - b1 > 0 and c2 - c1 > 0):
    d = (b2 - b1) + (c2 - c1)
    print(d)
elif (a2 - a1 > 0 and b2 - b1 <= 0 and c2 - c1 > 0):
    d = (a2 - a1) + (c2 - c1)
    print(d)
elif (a2 - a1 > 0 and b2 - b1 > 0 and c2 - c1 <= 0):
    d = (a2 - a1) + (b2 - b1)
    print(d)
elif (a2 - a1 <= 0 and b2 - b1 <= 0 and c2 - c1 > 0):
    d = c2 - c1
    print(d)
elif (a2 - a1 <= 0 and b2 - b1 > 0 and c2 - c1 <= 0):
    d = b2 - b1
    print(d)
elif (a2 - a1 > 0 and b2 - b1 <= 0 and c2 - c1 <= 0):
    d = a2 - a1
    print(d)
else:
    d = (a2 - a1) + (b2 - b1) + (c2 - c1)
    print(d)
