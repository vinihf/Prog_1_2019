n = 0
for n in range(10):
    n = n + 1
    if n % 2 != 0:
        continue # para aqui
    print('Número é ' + str(n))
print('Fora do loop')