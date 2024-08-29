seq = list(input())
rep = [1]
s = 1
for i in range(len(seq)):
    if (i == len(seq)-1):
        if (seq[i] == seq[i-1]):
            rep.append(s)
    elif (seq[i] == seq[i+1]):
        s = s + 1
    else:
        if (s > 1):
            rep.append(s)
            s = 1

print(max(rep))