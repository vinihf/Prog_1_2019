qtd = int(input("Informe o número de alunos:"))
for x in range(0,qtd,1):
    nome = input("Informe o nome do aluno")
    n1 = float(input("Informe o valor da nota 1:"))
    n2 = float(input("Informe o valor da nota 2:"))
    n3 = float(input("Informe o valor da nota 3:"))
    mediafinal = n1+n2+n3
    if mediafinal >=90:
        print(nome,"- A")
    elif mediafinal >=60 and mediafinal <90:
        print(nome,"- B")
    elif mediafinal >=30 and mediafinal <60:
        print(nome,"- C")
    else:
        print(nome,"- D")

























'''nome = input("Informe seu nome:")
idade = int(input("Informe sua idade:"))
print(nome," tem ",idade," anos.")
if idade >= 18:
    print(nome,"é maior de idade.")
else:
    print(nome,"é menor de idade.")
print("FIM")
'''