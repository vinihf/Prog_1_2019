faces = {5: 1601, 6: 1734, 2: 1696, 3: 1688, 4: 1633, 1: 1648}
#Converte as chaves em uma lista
#Retorna todas as chaves
chaves = list(faces.keys())

# Retorna todos valores
# faces.values()

#Ordena uma lista
chaves.sort()
#Percorre as chaves ordenadas
for key in chaves:
    print(key,"-",faces[key])
