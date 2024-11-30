import os

os.system("cls|| clear")
 
notas = []

for i in range(4):
    while True:
        nota = float(input(f"Digite a nota {i + 1}: "))
        
        # Verifica se a nota está no intervalo permitido
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        

# Calcula a média
media = sum(notas) / len(notas)

# notas
print("\nNotas:", notas)

# média final
print("Média Final:", media)

# menor nota 
print (f"Menor nota:", min(notas))

# maior nota
print (f"Maior nota:", max(notas))

# Ordem Crescente

