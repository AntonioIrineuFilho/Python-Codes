testes = []

while True:
    try:
        while True:
            ldif = []
            seq = list(map(int, input().split()))
            if (seq[0] == 0):
                break
            if (seq[0] == 1):
                testes.append('Alegre')
            elif (seq[0] == 2):
                if (max(seq[1], seq[2]) - min(seq[1], seq[2]) == 1):
                    testes.append('Alegre')
                else:
                    testes.append('Nao alegre')
            else:
                for i in range(1, seq[0]):
                    dif = max(seq[i], seq[i+1]) - min(seq[i], seq[i+1])
                    ldif.append(dif)
                for j in range(1, seq[0]):
                    if (j == seq[0]-1 and j in ldif):
                        testes.append('Alegre')
                    elif not (j in ldif):
                        testes.append('Nao alegre')
                        break
    except EOFError:
        break

for k in testes:
    print(k)

    