import os

os.system("cls|| clear")

# Inicializando variáveis.
notas = 0
QUANTIDADE_NOTAS = 4

def calcular_media(notas, quantidade_notas):
     media - notas / quantidade_notas
     return media

# Entrada
for i in range (QUANTIDADE_NOTAS):
    notas += float(input("Digite uma nota: "))

# Processamento
media = notas / QUANTIDADE_NOTAS

# Saída 
print(f"Média: {media}")