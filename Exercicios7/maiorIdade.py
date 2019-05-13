listaIdades = []
listaNomes = []
for x in range(0,2):
    nome = input("Informe seu nome:")
    idade = int(input("Informe sua idade:"))
    listaNomes.append(nome)
    listaIdades.append(idade)

for i in range(0,2):
    print(listaNomes[i]," (",listaIdades[i],")")
