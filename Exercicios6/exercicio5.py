def exercicio5(frase):
    frase = frase.lower()
    palavras = frase.split(" ")
    contaVogais = 0
    contaMais3 = 0
    for palavra in palavras:
        if len(palavra) > 3:
            contaMais3+=1
        if palavra[0] in "aeiou":
            contaVogais+=1
    print(contaMais3)
    print(contaVogais)