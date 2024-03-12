a, b, c, d = map(int, input().split())
if (a < b or a < c or a < d):
    if (b < c or b < d):
        if ((a + b) < c or (a + b) < d):
            print("S")
    elif (c < b or c < d):
        if ((a + c) < b or (a + c) < d):
            print("S")
elif (b < c or b < d):
    if(c < d):
        if ((b + c) < a or (b + c) < d):
            print("S")
    elif (d < c):
        if ((b + d) < a or (b + d) < c):
            print("S")
elif ((c + d) < a or (c + d) < b):
    print("S")
else:
    print("N")
