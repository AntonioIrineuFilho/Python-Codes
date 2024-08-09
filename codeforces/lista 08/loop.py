ppt = []

while True:
    n = int(input())
    if (n == 0):
        break
    mgn = list(map(int, input().split()))
    if (len(mgn) == 2):
        ppt.append(2)
    else:
        if (mgn[-1] > mgn[0]):
            p = 1
            x = min(mgn[0], mgn[1])
            for i in range(1, len(mgn)):
                if (i == len(mgn)-1):
                    if (x == mgn[i]):
                        y = x
                        if (p % 2 == 0):
                            x = max(mgn[i], mgn[0])
                            z = max(mgn[i-1], mgn[i])
                        else:
                            x = min(mgn[i], mgn[0])
                            z = min(mgn[i-1], mgn[i])
                        if (y != z):
                            p = p + 1
                    else:
                        if (p % 2 == 0):
                            x = min(mgn[i], mgn[0])
                        else:
                            x = max(mgn[i], mgn[0])
                        p = p + 1
                    break
                if (x == mgn[i]):
                    y = x
                    if (p % 2 == 0):
                        x = max(mgn[i], mgn[i+1])
                        z = max(mgn[i-1], mgn[i])
                    else:
                        x = min(mgn[i], mgn[i+1])
                        z = min(mgn[i-1], mgn[i])
                    if (y != z):
                        p = p + 1
                else:
                    if (p % 2 == 0):
                        x = min(mgn[i], mgn[i+1])
                    else:
                        x = max(mgn[i], mgn[i+1])
                    p = p + 1
            ppt.append(p)
        else:
            p = 1
            x = max(mgn[0], mgn[1])
            for i in range(1, len(mgn)):
                if (i == len(mgn)-1):
                    if (x == mgn[i]):
                        y = x
                        if (p % 2 == 0):
                            x = min(mgn[i], mgn[0])
                            z = min(mgn[i-1], mgn[i])
                        else:
                            x = max(mgn[i], mgn[0])
                            z = max(mgn[i-1], mgn[i])
                        if (y != z):
                            p = p + 1
                    else:
                        if (p % 2 == 0):
                            x = max(mgn[i], mgn[0])
                        else:
                            x = min(mgn[i], mgn[0])
                        p = p + 1
                    break
                if (x == mgn[i]):
                    y = x
                    if (p % 2 == 0):
                        x = min(mgn[i], mgn[i+1])
                        z = min(mgn[i-1], mgn[i])
                    else:
                        x = max(mgn[i], mgn[i+1])
                        z = max(mgn[i-1], mgn[i])
                    if (y != z):
                        p = p + 1
                else:
                    if (p % 2 == 0):
                        x = max(mgn[i], mgn[i+1])
                    else:
                        x = min(mgn[i], mgn[i+1])
                    p = p + 1
            ppt.append(p)

for j in ppt:
    print(j)