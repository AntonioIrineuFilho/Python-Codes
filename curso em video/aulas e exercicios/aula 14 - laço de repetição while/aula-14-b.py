r = 'S'
ni = 0
np = 0

while r == 'S':
    for i in range(0, 5):
        n = int(input('Digite um número: '))
        if (n % 2 == 0):
            np = np + 1
        else:
            ni = ni + 1
    r = input('Deseja continuar [S/N]? ').upper()

print('Foram informados {} números pares e {} números ímpares'.format(np, ni))