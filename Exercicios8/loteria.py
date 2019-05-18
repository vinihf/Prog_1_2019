from random import randint
sorteados = {}
for i in range(0,100000):
    sorteado = randint(1,60)
    sorteados[sorteado] = sorteados.get(sorteado,0)+1
print(sorteados)