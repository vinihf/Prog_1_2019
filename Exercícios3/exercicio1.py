valorTotal = float(input("Informe o valor total da compra: R$"))
parcelas = int(input("Informe em quantas parcelas deseja pagar: "))
valorParcela = valorTotal/parcelas
print(f"R${valorParcela:5.2f}")