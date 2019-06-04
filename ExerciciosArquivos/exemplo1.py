with open("arquivo.txt", 'w', encoding='utf-8') as arquivo:
    times = ['Grêmio','Juventude','Caxias','Internacional']
    for time in times: 
        arquivo.write(time+'\n')

