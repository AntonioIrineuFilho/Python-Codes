a, b, c = map(int, input('\033[1;37mDigite os três lados: ').split())
if (a + b > c and a + c > b and b + c > a):
    if (a == b and a == c):
        print('\033[1;32mOs três lados podem formar um triângulo do tipo \033[1;33mEQUILÁTERO\033[0;37m')
    elif (a == b or a == c or b == c):
        print('\033[1;32mOs três lados podem formar um triângulo do tipo \033[1;34mISÓSCELES\033[0;37m')
    else:
        print('\033[1;32mOs três lados podem formar um triângulo do tipo \033[1;35mESCALENO\033[0;37m')
else:
    print('\033[1;31mOs três lados não podem formar um triângulo\033[0;37m')