#Iniciando um dicionário com dados
nascimentos = {"Pessoa A":50,"Pessoa B":43,"Pessoa C":44}
#Imprimir as chaves
for el in nascimentos:
    print(el)
#Imprimir os valores
for elementos in nascimentos:
    print(nascimentos[elementos])
#Imprimir as chaves e os valores
for chave,valor in nascimentos.items():
    print(chave,"-",valor)