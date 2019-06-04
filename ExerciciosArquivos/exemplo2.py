with open('arquivo.txt','r', encoding='utf-8') as arquivo:
    #Lê todo conteúdo como uma string
    conteudoTodo = arquivo.read()
    #Lê o arquivo de linha em linha
    umaLinha = arquivo.readline()
    #Lê todas as linhas de um arquivo
    todasLinhas = arquivo.readlines()