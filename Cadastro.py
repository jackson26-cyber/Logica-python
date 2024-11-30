import os

os.system("cls|| clear")

# Definindo o login e senha.
login_cadastrado = "Jackson"
senha_cadastrada = "33900253"
tentativas = 0

# Entrada
while True:
    login = input ("Digite seu login: ")
    senha = input ("Digite seu senha: ")

# Processamento
    if login == login_cadastrado and senha == senha_cadastrada:
        print("Acesso ao sistema!")
        break
    
    if tentativas >= 3:
        print("Permitido apenas 3 tentativas!")
        break

# Saída

