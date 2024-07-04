def media_ponderada(v1, p1, v2, p2):
    media = (v1*p1 + v2*p2)/(p1+p2)
    return media

v1, p1 = map(int, input().split())
v2, p2 = map(int, input().split())

print(media_ponderada(v1, p1, v2, p2))
