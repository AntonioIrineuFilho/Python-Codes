estado = {}
brasil = []

for i in range(0, 3):
    estado['UF'] = input('UF: ')
    estado['Sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())

for j in brasil:
    for k, l in j.items():
        print(f'{k} = {l}')