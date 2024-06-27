import random

li = []

for i in range(0, 5):
    x = random.randint(0, 100)
    li.append(x)

tupla = tuple(li)

print(f'A tupla gerada aleatoriamente foi: {tupla}')
print(f'Maior valor: {sorted(tupla)[len(tupla)-1]}')
print(f'Menor valor: {sorted(tupla)[0]}')
    
