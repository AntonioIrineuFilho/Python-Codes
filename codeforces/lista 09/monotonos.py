n = int(input())
seq = list(input().lower().strip())

if (seq[0] == 'a' and seq[1] == 'a'):
    s = 1
else:
    s = 0
    
for i in range(1, n):
    if (i == n-1):
        if (seq[i] == 'a' and seq[i-1] == 'a'):
            s = s + 1
    elif (seq[i] == 'a' and seq[i+1] == 'a'):
        s = s + 1
    elif (seq[i] == 'a' and seq[i-1] == 'a' and seq[i+1] == 'b'):
        s = s + 1

print(s)

