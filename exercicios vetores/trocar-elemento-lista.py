li = list(map(int, input().split()))
e1 = li[0]
e2 = li[1]
li.remove(li[0])
li.remove(li[0])
li.insert(0, e2)
li.insert(1, e1)
print(li)