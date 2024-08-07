h, q = map(int, input().split())
altura_canos = list(map(int, input().split()))

for i in range(len(altura_canos)):
    if (i == len(altura_canos)-1):
        print('YOU WIN')
    elif not (max(altura_canos[i], altura_canos[i+1]) - min(altura_canos[i], altura_canos[i+1]) <= h):
        print('GAME OVER')
        break