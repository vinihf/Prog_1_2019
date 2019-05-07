def reverso(palavra):
    return palavra[::-1]


def palindromo(palavra):
    if palavra == reverso(palavra):
        return "É um palíndromo"
    else:
        return "Não é um palíndromo"




word = input("Informe uma palavra:")
print(palindromo(word))