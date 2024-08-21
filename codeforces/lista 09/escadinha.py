n = int(input())
seq = list(map(int, input().split()))
s = 0

if (len(seq) == 1 or len(seq) == 2):
    print('1')
else:
    dif = seq[1] - seq[0]
    for i in range(len(seq)):
        if (i == len(seq)-1):
            s = s + 1
        elif (seq[i+1] - seq[i] != dif):
            dif = seq[i+1] - seq[i]
            s = s + 1
    print(s)
