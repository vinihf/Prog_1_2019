lst = input().split(" ")
cod = int(lst[0])
qtd = int(lst[1])
tabela = {1:4.0,2:4.5,3:5.0,4:2.0,5:1.5}
price = tabela.get(cod)*qtd
print('Total: R$ %.2f' % price)