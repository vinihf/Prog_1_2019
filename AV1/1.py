elevador = 0

while True:
    peso = int(input("Informe o peso do indivíduo:"))
    if (peso+elevador)>500:
        print("Peso excedido")
        break
    else:
        elevador+=peso
