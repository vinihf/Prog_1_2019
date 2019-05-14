#Iniciando um dicionário vazio
nascimentos = {}
while True:
    nome = input("Informe seu nome:")
    idade = int(input("Informe sua idade:"))
    #Inserindo um dado em um dicionário
    nascimentos[nome] = idade
    continuar = input("Continuar? S/N")
    if continuar == "N":
        break
#Impressão do dicionário completo    
print(nascimentos)