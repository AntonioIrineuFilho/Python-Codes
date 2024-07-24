alfa = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
num = '0 1 2 3 4 5 6 7 8 9'.split()

exp = input('Digite a expressão: ').strip().lower()
l_exp = []

for i in range(len(exp)):
    if not (exp[i] == ' '):
        l_exp.append(exp[i])

if ('(' not in l_exp and ')' not in l_exp):
    print('Expressão válida')
else:
    if (l_exp.count('(') == l_exp.count(')')):
        indices_open = []
        indices_close = []
        cont = 0
        for i in range(len(l_exp)):
            if (l_exp[i] == '('):
                indices_open.append(i)
            if (l_exp[i] == ')'):
                indices_close.append(i)
        for i in range(len(indices_open)):
            if (indices_open[i] < indices_close[i]):
                cont = cont + 1
            if (indices_open[i] + 1 == indices_close[i]):
                cont = cont - 1
            if (l_exp[indices_open[i] + 1] not in alfa and l_exp[indices_open[i] + 1] not in num and not l_exp[indices_open[i] + 1] == '-'):
                cont = cont - 1
            if (l_exp[indices_close[i] - 1] not in alfa and l_exp[indices_close[i] - 1] not in num and not l_exp[indices_close[i] - 1] == '-'):
                cont = cont - 1
        if (cont == len(indices_open)):
            print('Expressão válida')
        else:
            print('Expressão inválida')
    else:
        print('Expressão inválida')