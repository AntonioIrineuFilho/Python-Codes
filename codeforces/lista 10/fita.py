n = int(input())
fita = list(map(int, input().split()))
tons = []

if (fita.count(-1) == len(fita)):
    for i in range(len(fita)):
        tons.append(0)
    print(*tons)
else:
    for i in range(len(fita)):
        if (fita[i] == 0):
            tons.append(0)
        else:
            epd = 1
            dpe = 1
            zero1 = False
            zero2 = False
            for j in range(i+1, len(fita)):
                if (fita[j] == 0):
                    zero1 = True
                if not (fita[j] == 0):
                    epd = epd + 1
                else:
                    break
            for k in range(i-1, -1, -1):
                if (fita[k] == 0):
                    zero2 = True
                if not (fita[k] == 0):
                    dpe = dpe + 1
                else:
                    break
            if (epd > 9):
                epd = 9
            if (dpe > 9):
                dpe = 9
            if (i == 0 and zero1):
                tons.append(epd)
            elif (i == len(fita)-1 and zero2):
                tons.append(dpe)
            else:
                if (zero1 and zero2):
                    tons.append(min(epd, dpe))
                elif (zero1):
                    tons.append(epd)
                elif (zero2):
                    tons.append(dpe)

    print(*tons)