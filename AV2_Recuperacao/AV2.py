#     Avaliação Individual de recuperação 2 (10 pontos)

#  Nesta avaliação você deverá implementar cada uma das funções abaixo.
#  Durante o desenvolvimento você pode executar o arquivo para fazer testes normalmente.
#  A avaliação é individual e com consulta offline. Portanto, considera-se que deve
#  ser realizada de forma individual.
#  É importante que o retorno das funções implementadas seja exatamente o solicitado. 
#  Caso contrário, o algoritmo de avaliação não irá corrigir corretamente.
#
#  Boa avaliação pra você!

# imprime
# 
# Faça uma função que retorne a mensagem "Eu sei programar!"
#
# Pontuação: 1

def imprime():
      return


# triplo
# 
# Faça uma função que recebe um valor inteiro (n) por parâmetro e
# retorne o triplo desse valor
#
# Pontuação: 1

def triplo(n):
      return 

# metade
# 
# Faça uma função que recebe uma string (t, sempre com mais de 2 caracteres) por parâmetro e 
# retorne a string sem o primeiro e o último caractere.
#
# Pontuação: 2

def metade(t):
      return 

# mediana
# 
# Faça uma função que recebe uma lista ordenada de valores inteiros e retorne a mediana
# deste conjunto de valores. 
# Considere que: se o número de elementos é ímpar, a mediana é o valor do meio. Se o
# número de elementos é par, a mediana é a soma dos dois elementos do meio divididos por 2
#
# Exemplo com quantidade de valores ímpar: [1,2,3,4,5] = 3
# Exemplo com quantidade valores par: [1,2,4,5] = (2+4)/2 = 3
#
# Pontuação: 3

def mediana(lista):
      return

# mais_quente
# 
# Faça uma função que recebe um dicionário com as temperaturas 
# máximas registradas para cada dia útil da semana e retorne o dia em que
# foi registrada a maior dessas temperaturas. Não há nestes dicionários temperaturas
# repetidas.
#
# Exemplo: {"segunda":20.0,"terça":25.1,"quarta":24.2,"quinta":25.5,"sexta":26.6}
#
# Pontuação: 3

def mais_quente(dic):
      return

'''
NÃO ALTERE O CÓDIGO A PARTIR DESTE COMENTÁRIO. 
QUALQUER ALTERAÇÃO PODE COMPROMETER O PROCESSO DE CORREÇÃO
'''
def test(obtido, esperado):
      return obtido == esperado

def main():
      pontuacao = 0
      if test(imprime(),"Eu sei programar!"):
            pontuacao+=1
            print(pontuacao)
      if all([test(triplo(1),3),test(triplo(2),6),test(triplo(10),30),test(triplo(40),120)]):
            pontuacao+=1
            print(pontuacao)
      if all([test(metade("ola"),'l'),test(metade('cachorro'),'achorr'),test(metade('python'),'ytho')]):
            pontuacao+=2
            print(pontuacao)
      if all([test(mediana([1,2,3,4,5]),3.0),test(mediana([3,3,4,5,6]),4.0),test(mediana([1,2,3,4,5,6]),3.5),test(mediana([3,4,5,6,6,6,6,7,8,91]),6.0)]):
            pontuacao+=3
            print(pontuacao)
      teste_semana = {"segunda":20.0,"terça":25.1,"quarta":27.2,"quinta":25.5,"sexta":26.6}
      if test(mais_quente(teste_semana),"quarta"):
            pontuacao+=3
      print("Pontuação:",pontuacao)

if __name__ == '__main__':
      main()