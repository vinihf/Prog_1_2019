salario = float(input())
if salario <= 400.00:
    r = 0.15
elif salario <= 800.00:
    r = 0.12
elif salario <= 1200.00:
    r = 0.1
elif salario <= 2000.00:
    r = 0.07
else:
    r = 0.04
print("Novo salario: %.2f" % (salario+(salario*r)))
print("Reajuste ganho: %.2f" % (salario*r))
print("Em percentual: %d %%" % (r*100))