from random import randint

sorteio = randint(1,10)
continua = True
chutes = 0
while continua == True:
    valor = int(input("Informe um valor:"))
    if sorteio == valor:
        chutes = chutes+1
        continua = False
    else:
        chutes = chutes+1
print("O número sorteado foi",sorteio,".")
print("Foram necessários",chutes,"chutes.")




















'''from random import randint

continua = True
chances = 0
sorteio = randint(1,10)
while continua == True:
    chute = int(input("Qual foi o número sorteado?"))
    if chute == sorteio:
        chances = chances+1
        continua = False
    else:
        chances = chances+1
print("O número sorteado foi:",sorteio,".")        
print("Foram necessárias",chances,"chances para vencer.")
'''