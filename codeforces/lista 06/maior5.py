def maior5(a, b, c, d, e):
    if (a >= b and a >= c and a >= d and a >= e):
        return a
    elif (b >= c and b >= d and b >= e):
        return b
    elif (c >= d and c >= e):
        return c
    elif (d >= e):
        return d
    else:
        return e

print(maior5(10, 40, -80, 120, -160))