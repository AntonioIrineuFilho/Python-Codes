n = int(input('Digite um valor: '))
f = 1
# for i in range(n, 0, -1):
#    f = f * i
# print(f)
while n != 0:
    f = f * n
    n = n - 1
print(f)