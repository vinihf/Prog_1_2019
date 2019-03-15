nome = input("Informe o nome do aluno:")
nota = float(input("Informe a nota final:"))
presenca = float(input("Informe o percentual de presença:"))
if nota >= 7.0 and presenca >=75.0:
    print(nome," foi aprovado!")
else:
    print(nome," foi reprovado!")