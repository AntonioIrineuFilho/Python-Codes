li = list(map(int, input().split()))
pue = len(li) - 1
e1 = li[0]
ue = li[pue]
li.remove(li[0])
li.remove(li[pue-1])
li.insert(0, ue)
li.insert(pue, e1)
print(li)