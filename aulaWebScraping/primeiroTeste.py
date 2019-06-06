from bs4 import BeautifulSoup

with open('./pagina/index.html','r') as arquivo:
    html = BeautifulSoup(arquivo.read(), 'html.parser')

print(html.title.text)
nome = html.find(class_='name_user')

print(nome.text)
atividades = html.find_all(class_='item')

for atividade in atividades:
    print(atividade.text)

