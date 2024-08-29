n = int(input())
seq = []
rep = []
seqmd = [2]
for i in range(0, n):
    x = int(input())
    if (x in seq and x not in rep):
        rep.append(x)
    seq.append(x)

if (seq.count(seq[0]) == len(seq)):
    print('1')
elif (len(rep) == 0):
    print('2')
else:
    for i in range(len(rep)):
        for j in range(seq.index(rep[i])+1, len(seq)):
            s = 2
            n1 = rep[i]
            n2 = seq[j]
            if (n1 != n2):
                for k in range(j+1, len(seq)):
                    if (s == 2):
                        if (seq[k] == n1):
                            s = s + 1
                    elif ((s + 1) % 2 == 0 and s > 2):
                        if (seq[k] == n2):
                            s = s + 1
                    elif (s % 2 == 0 and s > 2):
                        if (seq[k] == n1):
                            s = s + 1
                seqmd.append(s)
    print(max(seqmd))