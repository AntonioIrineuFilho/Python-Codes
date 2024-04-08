x = [(1,1), (1, 2), (2,2), (2,3), (3,3)]
y = [1, 2, 3]
z = []
for a, b in range(len(x)):
    if (x[a] == (y[a], y[a]) or x[a] == (y[b], y[b])):
        z.append(x[a])
    elif (x[b] == (y[a], y[a]) or x[b] == (y[b], y[b])):
        z.append(x[b])
if ()
