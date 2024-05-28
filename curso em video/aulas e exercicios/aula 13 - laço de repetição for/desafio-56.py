s = 0
m = 0
maior = 0

for i in range(1, 5):
    nome = input('Nome da pessoa {}: '.format(i)).strip().upper()
    idade = int(input('Idade da pessoa {}: '.format(i)))
    gen = input('Gênero da pessoa {}: '.format(i)).strip().upper()
    s = s + idade
    if (idade < 20 and gen == 'F'):
        m = m + 1
    if (i == 1 and gen == 'M'):
        maior = idade
        maior_nome = nome
    if (gen == 'M'):
        if(idade > maior):
            maior = idade
            maior_nome = nome

print('A média das idades digitadas é {:.1f} anos'.format(s/4))
print('O homem mais velho se chama {} e possui {} anos'.format(maior_nome, maior))
print('Existem {} mulheres com menos de 20 anos'.format(m))



