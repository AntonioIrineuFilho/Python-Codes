def media_lista(lista):
    s = 0
    q = 0
    for i in range(len(lista)):
        s = s + lista[i]
        q = q + 1
    return s//q


li = list(map(int, input().split()))

print(media_lista(li))
