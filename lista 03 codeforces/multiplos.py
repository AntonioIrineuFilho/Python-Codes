a = int(input())
b = int(input())
if(a > b):
    if(a % b == 0):
        print("Multiplos")
    else:
        print("Nao Multiplos")
else:
    if(b % a == 0):
        print("Multiplos")
    else:
        print("Nao multiplos")