dif_horarios = []

while True:
    ha, ma, hp, mp = map(int, input().split())
    if (ha == 0 and ma == 0 and hp == 0 and mp == 0):
        break
    atual = ha*60 + ma
    prog = hp*60 + mp
    dif = prog - atual
    if (dif < 0):
        dif_horarios.append(dif + 1440)
    else:
        dif_horarios.append(dif)

for i in dif_horarios:
    print(i)
    

