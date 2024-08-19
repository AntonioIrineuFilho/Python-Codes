cifra = list(input().upper().strip())
palavra = list(input().upper().strip())
s = 0

for i in range(0, (len(cifra)-len(palavra))+1):
    for j in range(len(palavra)):
        if (palavra[j] == cifra[j+i]):
            break
        elif (j == len(palavra)-1):
            s = s + 1

print(s)
