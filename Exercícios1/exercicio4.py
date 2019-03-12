precoCapa = 24.95
quantidade = 60
desconto = 0.4
transportePrimeiro = 3.00
transporteDemais = 0.75

precoAtacado = ((precoCapa-(precoCapa*desconto))*quantidade) + transportePrimeiro + (transporteDemais*quantidade)
print("O preço total é de R$ %.2f" %precoAtacado)
