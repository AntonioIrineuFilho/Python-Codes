a, b, c = map(int, input().split())
if not ((a + b) > c and (a + c) > b and (b + c) > a):
    print("n")
elif (a >= b and a >= c):
    if ((b ** 2 + c ** 2 - a ** 2) == 0):
        print("r")
    elif ((b ** 2 + c ** 2 - a ** 2) > 0):
        print("a")
    else:
        print("o")
elif (b >= a and b >= c):
    if ((a ** 2 + c ** 2 - b ** 2) == 0):
        print("r")
    elif ((a ** 2 + c ** 2 - b ** 2) > 0):
        print("a")
    else:
        print("o")
elif (c >= a and c >= b):
    if ((a ** 2 + b ** 2 - c ** 2) == 0):
        print("r")
    elif ((a ** 2 + b ** 2 - c ** 2) > 0):
        print("a")
    else:
        print("o")