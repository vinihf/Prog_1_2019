with open('arquivo.txt','a',encoding='utf-8') as arquivo:
    while True:
        time=input("Nome de um time:")
        if time=='nenhum':
            break
        arquivo.write(time+"\n")
        
