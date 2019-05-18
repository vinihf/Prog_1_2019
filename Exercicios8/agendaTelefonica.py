def inserirContato(agenda,nome,numero):
    agenda[nome] = numero

def removerContato(agenda,nome):
    if nome in agenda:
        del agenda[nome]
        return True
    return False

def alterarContato(agenda,nome,numero):
    if nome in agenda:
        agenda[nome] = numero
        return True
    return False

def exibirContatos(agenda):
    for nome,numero in agenda.items():
        print(nome," - ",numero)

def pesquisarContato(agenda,nome):
    if nome in agenda:
        return agenda[nome]
    return False

agenda = {}
while True:
    print("AGENDA TELEFONICA")
    print("[I]nserir Contato")
    print("[R]emover Contato")
    print("[A]lterar Contato")
    print("[E]xibir Contatos")
    print("[P]esquisar Contato")
    print("[S]air")
    opcao = input("Qual é a opção?")
    if opcao =="I":
        nome = input("Informe o nome:")
        numero = input("Informe o número:")
        inserirContato(agenda,nome,numero)
    if opcao == "R":
        nome = input("Deseja remover qual contato?")
        if removerContato(agenda,nome):
            print("Contato removido")
        else:
            print("Contato inexistente")
    if opcao == "A":
        nome = input("Deseja alterar qual contato?")
        numero = input("Qual é o novo número?")
        if alterarContato(agenda,nome,numero):
            print("Contato alterado.")
        else:
            print("Contato inexistente")
    if opcao == "E":
        exibirContatos(agenda)
    if opcao == "P":
        nome = input("Informe o nome:")
        resultado = pesquisarContato(agenda,nome)
        if resultado == False:
            print("Contato não encontrado.")
        else:
            print(nome," - ",resultado)
    if opcao == "S":
        break