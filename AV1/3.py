aplicacao = 10000
carro = 12000
meses = 0
while carro > aplicacao:
    aplicacao += (aplicacao*0.007)
    carro += (carro*0.004)
    meses+=1
    print(f'{aplicacao:10.2f} - {carro:10.2f}')
print(meses)