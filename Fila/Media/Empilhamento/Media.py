import os

# Função. 
def logo_senai():
    os.system("cls|| clear")
    print("=== SENAI ===")





# Entrada. 
# Constante.
QUANTIDADE_DE_NOTAS = 4

# Vetor / Lista
lista_de_notas = []

# Processamento e entrada
print("===SENAI===")
for i in range(QUANTIDADE_DE_NOTAS):
    nota = float(input("Digite uma nota: "))
    lista_de_notas.append(nota)

# Cálculo da média
soma = sum(lista_de_notas) # Função com retorno. 
media = soma / QUANTIDADE_DE_NOTAS

# Saída
for cada_nota in lista_de_notas:
    print(f"Nota: {cada_nota}")

print(f"Média: {media}")