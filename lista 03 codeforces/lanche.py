c, q = map(float, input().split())
if(c == 1):
    preco = q * 4
    print("Total: R$", "{:.2f}".format(preco))
elif(c == 2):
    preco = q * 4.5
    print("Total: R$", "{:.2f}".format(preco))
elif(c == 3):
    preco = q * 5
    print("Total: R$", "{:.2f}".format(preco))
elif(c == 4):
    preco = q * 2
    print("Total: R$", "{:.2f}".format(preco))
else:
    preco = q * 1.5
    print("Total: R$", "{:.2f}".format(preco))

