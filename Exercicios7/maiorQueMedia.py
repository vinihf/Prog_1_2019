lista = []

while True:
    valor = int(input("Valor:"))
    if valor < 0:
        break
    lista.append(valor)

soma = 0 

for v in lista:
    soma = soma+v

media = soma/len(lista)

for v in lista:
    if v > media:
        print(v)





        
