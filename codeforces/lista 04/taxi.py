a, g, ra, rg = map(float, input().split())
x = ra / a
y = rg / g
if (y >= x):
    print("G")
else:
    print("A")