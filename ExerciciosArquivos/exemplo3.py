with open('arquivo2.txt','r',encoding='utf-8')as arquivo:
    conteudo = arquivo.readlines()
    for linha in conteudo:
        linguagens = linha.strip().split("#")
        print(linguagens[0])
        print(linguagens[1])
