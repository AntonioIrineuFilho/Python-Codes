l1 = list(map(int, input().split()))
l2 = sorted(l1)
if (l2[0] % 2 == 0):
    print(l2[0])
elif (l2[1] % 2 == 0):
    print(l2[1])
elif (l2[2] % 2 == 0):
    print(l2[2])
elif (l2[3] % 2 == 0):
    print(l2[3])
else:
    print('0')