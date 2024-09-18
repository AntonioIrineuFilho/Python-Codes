q = int(input('Digite a quantidade de produtos: '))
votos = list(map(int, input('Digite os votos de cada um, em ordem: ').split()))

# def most_chosen(q, votos):
#     alfa = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     maior = 0
#     dic_most_chosen = {}
#     maiores = []
#     indices = []
#     for i in range(len(votos)):
#         if (votos[i] > maior):
#             maior = votos[i]
#     for j in range(len(votos)):
#         if (votos[j] == maior):
#             maiores.append(votos[j])
#             indices.append(j)
#     for k in range(len(maiores)):
#         dic_most_chosen[f'Produto {alfa[indices[k]]}'] = maiores[k]
#     return dic_most_chosen

# print(most_chosen(q, votos))

    
def dic_most_chosen_sorted(q, votos):
    alfa = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    dic_most_chosen = {}
    for i in range(len(votos)):
        dic_most_chosen[f'Produto {alfa[i]}'] = votos[i]
    dic_most_chosen_sorted = dict(sorted(dic_most_chosen.items(), key=lambda item: item[1]))
    return dic_most_chosen_sorted

print(dic_most_chosen_sorted(q, votos))