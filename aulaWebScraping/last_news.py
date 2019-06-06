import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.python.org/')
html = BeautifulSoup(r.content,"html.parser")
container = html.find(class_='shrubbery')
titulo = container.find(class_='widget-title')
print("Título:"+titulo.text)
menu = container.find(class_='menu')
itens = menu.find_all('li')
for item in itens:
    print('========')
    print(item.a.get('href'))