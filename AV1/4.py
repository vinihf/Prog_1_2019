n1 = float(input("Informe a N1:"))
n2 = float(input("Informe a N2:"))
n3 = float(input("Informe a N3:"))
media = (n1+n2+n3)/3.0
ch = int(input("Quantas aulas a disciplina teve no total?"))
pre = int(input("Quantas aulas o aluno esteve presente?"))
pp = (100*pre)/ch
if media >=7.0 and pp >= 75:
    print("Aprovado")
else:
    print("Reprovado")