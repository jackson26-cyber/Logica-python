import os
os.system("cls|| clear")
# Algoritmo para ler a nota do aluno e validar a entrada

while True:
    # Solicita a nota ao usuário
    nota = input("Digite a nota do aluno (entre 0 e 10): ")
    
    # Verifica se a entrada é um número inteiro
    if nota.isdigit():
        nota = int(nota)  # Converte a entrada para inteiro
        # Verifica se a nota está dentro do intervalo válido
        if 0 <= nota <= 10:
            print(f"A nota informada foi: {nota}")
            break  # Encerra o loop se a nota for válida
        else:
            print("Nota inválida! A nota deve estar entre 0 e 10. Tente novamente.")
    else:
        print("Entrada inválida! Por favor, digite um número inteiro.")
