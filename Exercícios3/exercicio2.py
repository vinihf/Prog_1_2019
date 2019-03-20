nome = input("Informe seu nome:")
premio = 0
resp1 = int(input("10 * 5 = ?"))
if resp1 == 50:
    print("Acertou!")
    premio = 250000
else:
    print("Errou!")
resp2 = int(input("10 * 4 = ?"))
if resp2 == 40:
    print("Acertou!")
    premio = premio + 250000
else:
    print("Errou!")
resp3 = int(input("10 * 3 = ?"))
if resp3 == 30:
    print("Acertou!")
    premio = premio + 250000
else:
    print("Errou!")
resp4 = int(input("10 * 2 = ?"))
if resp4 == 20:
    print("Acertou!")
    premio = premio + 250000
else:
    print("Errou!")
print(nome,"ganhou R$",premio)


