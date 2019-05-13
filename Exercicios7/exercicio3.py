def quantosAs(nome):
    contador = 0
    nome = nome.lower()
    for letra in nome:
        if letra == 'a':
            contador+=1
    return contador


nome = input("Informe o seu nome:")
print(quantosAs(nome))