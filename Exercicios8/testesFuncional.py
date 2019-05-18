from functools import reduce

listas = [1,3,5,2,3,6,8,11,9]

mapa = list(map(lambda x:x*2,listas))
filtro = list(filter(lambda x:x%2==0,listas))
reduzir = reduce(lambda a,b:a+b,listas)

print(mapa)
print(filtro)
print(reduzir)