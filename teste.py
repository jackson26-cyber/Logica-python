#Função para monstar o menu ao usuário
def mostrar_menu():
    print("Menu de Opções: ")
    print("1 - Cadastar novo usuário: ")
    print("2 - Listar todos os usuários cadastrado")
    print("3 - Sair")


#Função para Cadastro dos Usuários
def cadastrar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ") #Declarando uma variável para receber o nome
    idade = input("Digite a idade do usuário") #Declarando uma variável para receber a idade
    email = input("Digite seu e-mail")          #Declarando uma variável para receber o e-mail

    usuario = {"nome":nome, "idade":idade, "email": email} #vetor com os dados do usuário
    usuarios.append(usuario)                             #adicionando o usuário cadastrado no final de uma lista
    print("Usuário cadastrado com sucesso")             #mostrar na tela mensagem de concluido

#Função para Listar os Usuários na Tela
def listar_usuarios(usuarios):
    if len(usuarios) == 0:                      #Lógica SE
        print("Nenhum usuário cadastrado")      #mostrar na tela
    else:                                       #SENAO
        print("Lista dos usuários cadastrado")

        #ESTRUTURA DE REPETIÇÃO

        #ENUMERANTE: Retorna a quantidade de dados de um vetor em uma lista
        for i, usuarios in enumerate(usuarios, start=1):
            print(f"Usuário: {i}",)        #Mostrar na tela a posição de cadastro
            print(f"Nome :{usuarios['nome']} ")
            print(f"Idade :{usuarios['idade']} ")    
            print(f"Email :{usuarios['email']} ")      