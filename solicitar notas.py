import os

os.system("cls|| clear")

# Lista de armazenamento
notas = []

while True:
    # Solicita nota ao usuário
    nota = float(input("Digite uma nota: "))
    
    if nota < 0:
        break

    # Adiciona a nota à lista
        notas.append(nota)

# Calcula a média, se houver notas
if notas:
    media = sum(notas) / len(notas)
else:
    media = 0

# Exibir nota final
print("\nNotas final:", notas)

# Exibe a média das notas
print("Média:", media)

