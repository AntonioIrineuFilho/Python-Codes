kml = int(input())
dist = int(input())
t = int(input())
x = float((dist / kml) - t)
if (x < 0):
    print("0.0")
else:
    print("{:.1f}".format(x))