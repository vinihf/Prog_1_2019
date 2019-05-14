faces = {5: 1601, 6: 1734, 2: 1696, 3: 1688, 4: 1633, 1: 1648}
#Deletar por chave
del faces[5]
print(faces)
#Remover e retornar por chave
faces.pop(6)
print(faces)
#Remover e retonar item aleatório
faces.popitem()
print(faces)
#Limpar o dicionário
faces.clear()
print(faces)