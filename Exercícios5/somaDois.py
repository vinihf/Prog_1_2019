soma = 0 
continua = True
while continua == True:
    v1 = int(input("Informe um valor:"))
    v2 = int(input("Informe um valor:"))
    soma = v1 + v2
    if soma < 0:
        continua = False
        print("A soma é negativa")
    else:
        print(soma)