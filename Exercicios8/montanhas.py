import requests
from bs4 import BeautifulSoup
import json

conteudo = requests.get("https://en.wikipedia.org/wiki/List_of_mountains_by_elevation")
html = BeautifulSoup(conteudo.content, 'html.parser')
linhas = html.find_all("tr")
dados = []
montanhas = {}
for linha in linhas:
    dados.append(linha.find_all('td'))
for i in range(1,len(dados)):
    if len(dados[i])!=0:
        if dados[i][0].find('a'):
            montanhas[dados[i][0].find('a').text] = dados[i][1].text.replace(",","")
        else: 
            montanhas[dados[i][0].text] = dados[i][1].text.replace(",","")
with open('data.json', 'w') as outfile:  
   json.dump([{'nome': k, 'altura': float(v)} for k,v in montanhas.items()], outfile)