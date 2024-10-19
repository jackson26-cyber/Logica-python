import os
os.system("cls|| clear")
from Media import QUANTIDADE_DE_NOTAS

# Função. 
def logo_senai():
    
    print("=== SENAI ===")

def calcular_media(lista_notas):
    # Processamento.
    soma =sum(lista_notas) # Função com retorno.
    media_calcular = soma / QUANTIDADE_DE_NOTAS
    return media_calcular

# Entrada. 
# Vetor / Lista
lista_de_notas = []

# Processamento e entrada
for i in range(QUANTIDADE_DE_NOTAS):
    logo_senai() # Função sem retorno.
    nota = float(input("Digite uma nota: "))
    lista_de_notas.append(nota)

# Cálculo da média

media = calcular_media(lista_de_notas) # Função com 

# Saída
for cada_nota in lista_de_notas:
    print(f"Nota: {cada_nota}")

print(f"Média: {media}")