soma = 0
while True:
    valor = int(input("Informe um valor ímpar:"))
    if valor%2!=0:
      soma = soma + valor
    else:
        break
print(soma)
