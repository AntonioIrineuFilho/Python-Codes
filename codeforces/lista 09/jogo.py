jog, r = map(int, input().split())
pontos = list(map(int, input().split()))
tp = []

for i in range(0, jog):
    s = pontos[i]
    indice = i
    for j in range(1, r):
            indice = indice + jog
            s = s + pontos[indice]
    tp.append(s)

if (tp.count(max(tp)) > 1):
    for i in range(len(tp)):
        if (tp[i] == max(tp)):
             ind_maior = i
    print(ind_maior+1)      
else:
    print(tp.index(max(tp))+1)
