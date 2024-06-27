# tuplas -> variaveis compostas, variaveis em que é possível armazenar vários dados
# indices -> forma de identificar dados dentro da tupla, por meio da posição
# ex: dado[0] -> dado(variavel), [0](indice)
# em tuplas/listas é possivel realizar fatiamento(como em strings)
# ex: dado[0:2] -> mapeia os dados da variavel dado do indice 0 até o 1
# ao utilizar o operador de soma com tuplas, ocorre a concatenação das mesmas

dado = (0, 1, 2, 3, 4)
print(dado[0:3])

a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
c = a + b
print(c)