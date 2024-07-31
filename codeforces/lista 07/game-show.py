n = int(input())
s = 100
lc = []
lp = [100]
for i in range(0, n):
    c = int(input())
    lc.append(c)
for j in lc:
    s = s + j
    lp.append(s)
    
print(max(lp))



