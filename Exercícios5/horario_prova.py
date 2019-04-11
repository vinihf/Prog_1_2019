nome = input("Nome do filme:")
horaI = int(input("Horario de início:"))
minutoI = int(input("Minutos de início:"))
duracao = int(input("Duração do filme:"))
horaD = duracao//60
minutoD = duracao%60
horaI = horaD+horaI
minutoI = minutoD+minutoI
