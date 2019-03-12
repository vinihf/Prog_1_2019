A = 3
B = 2.1
C = "Python"

#Usando print e concatenando valores com vírgula(,)
print("A =",A,"B =",B,"C =",C)

#Usando % para identificar valores
# %d - para inteiros
# %s - para strings
# %f - para ponto flutuante
# %.2f - para ponto flutuante com limitação de casas decimais

print("A = %d B = %f C = %s" % (A,B,C))
print("B = %.3f" % B)


#Usando f'
#Aqui, usamos o ":" para indicar quantos caracteres irá utilizar e o ponto para
#limitar as casas decimais

print(f"A = {A} B = {B:.4f} C = {C}")



