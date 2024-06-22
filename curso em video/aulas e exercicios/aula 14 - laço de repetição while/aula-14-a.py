# o for precisa de um range, um limite especificado
# para girar um laço sem saber exatamente qual o limite, utiliza-se o while
# for = estrutura de repetição com variavel de controle
# while = estrutura de repetição com teste lógico

# i = 0
# while i < 10:
#    print(i)
#    i = i + 1
r = 'S'
ni = 0
np = 0

while r == 'S':
    n = int(input('Digite um número: '))
    r = input('Deseja continuar [S/N]? ').upper()
    if (n % 2 == 0):
        np = np + 1
    else:
        ni = ni + 1

print('Foram informados {} números pares e {} números ímpares'.format(np, ni))
