# é possivel adicionar outras listas em uma lista
# ao adicionar uma lista na outra, deve se utilizar dois indices para manipular os elementos
# o primeiro indice busca a sublista dentro da lista principal 
# o segundo indice busca um elemento da sublista



dados = ['Pedro', 25, 'Gabriel', 24, 'Joao', 67, 'Julia', 29, 'Carla', 40]
pessoas = []
for i in range(0, len(dados), 2):
        pessoas.append(dados[i:i+2])

pessoas[2][1] = 26
# a sublista de indice 2 é ['Joao', 67] e o elemento da sublista é a idade(67), que vai ser substituida por 26
print(pessoas)



