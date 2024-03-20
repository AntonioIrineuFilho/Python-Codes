a, b, c = map(int, input().split())
if not ((a + b) > c and (a + c) > b and (b + c) > a):
    print("n")
elif ((a == b and a == c and c == b) or (a == b or a == c or b == c)):
    print("a")
elif (a > b and a > c):
    if ((b ** 2 + c ** 2) == a ** 2):
        print("r")
    elif (b != c):
        print("o")
elif (b > a and b > c):
    if ((a ** 2 + c ** 2) == b ** 2):
        print("r")
    elif (a != c):
        print("o")
elif (c > a and c > b):
    if ((a ** 2 + b ** 2) == c ** 2):
        print("r")
    elif (a != b):
        print("o")