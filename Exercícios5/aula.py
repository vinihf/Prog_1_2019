soma = 0 
continua = True
while continua == True:
    v = int(input("Informe um valor:"))
    if v < 0:
        continua = False
    else:
        soma = soma + v
print(soma)