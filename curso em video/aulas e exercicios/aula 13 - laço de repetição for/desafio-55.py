# li = []

# for i in range(0, 5):
#    p = int(input('Digite um peso: '))
#    li.append(p)

# li_s = sorted(li)

# print('O maior peso informado é {}'.format(li_s[4]))
# print('O menor peso informado é {}'.format(li_s[0]))

for i in range(0, 5):
    p = int(input('Digite um peso: '))
    if (i == 0):
        a = p
    elif (i == 1):
        b = p
    elif (i == 2):
        c = p
    elif (i == 3):
        d = p
    else:
        e = p

maior = max(max(max(max(a, b), c), d), e)
menor = min(min(min(min(a, b), c), d), e)

print('O maior peso informado foi {}'.format(maior))
print('O menor peso informado foi {}'.format(menor))


