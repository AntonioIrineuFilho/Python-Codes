a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = []

if (len(a) <= len(b)):
    menor = a
    maior = b
else:
    menor = b
    maior = a

if (len(a) != len(b)):
    for i in range(len(menor)):
        s.append(a[i] + b[i])
    for c in range(len(menor), len(maior)):
        if (len(maior) == len(a)):
            s.append(a[c])
        else:
            s.append(b[c])
else:
    for i in range(len(a)):
        s.append(a[i] + b[i])

print(s)



