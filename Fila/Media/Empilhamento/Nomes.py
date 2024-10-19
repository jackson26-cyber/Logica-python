lista_nomes = []

# Solicitando dados. 
for i in range(4):
    nome = input(f"Digite o {i+1}º nome: ")
    lista_nomes.append(nome)

# Imprimindo os nomes
for i, cada_nome in enumerate(lista_nomes, start=1):
    print(f"{i}º nome: {cada_nome}")