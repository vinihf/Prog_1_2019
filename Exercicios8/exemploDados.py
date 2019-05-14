from random import randint
faces = {}
for x in range(0,10000):
    faceSorteada = randint(1,6)
    #A função get retorna um valor padrão para a posição no dicionário
    faces[faceSorteada] = faces.get(faceSorteada,0)+1
print(faces)
