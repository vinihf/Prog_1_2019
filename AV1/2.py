nomeMin = ''
idadeMin = 1000
for x in range(0,3):
    nome = input("Informe o nome:")
    idade = int(input("Informe a idade:"))
    if idade < idadeMin:
        idadeMin = idade
        nomeMin = nome
print(f'Nome: {nome} Idade {idade}')