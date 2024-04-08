li = list(map(int, input().split()))
n1 = li[0]
n3 = li[len(li) - 1]
if (len(li) % 2 == 0):
    if ((li[((len(li) // 2) - 1)] + li[(len(li) // 2)]) % 2 == 0):
        n2 = (li[((len(li) // 2) - 1)] + li[(len(li) // 2)]) // 2
    else:
        n2 = (li[((len(li) // 2) - 1)] + li[(len(li) // 2)]) / 2
else:
    n2 = li[len(li) // 2]
print('A soma entre o primeiro elemento, o elemento central e o último elemento é ', end = "")
print(n1 + n2 + n3)
