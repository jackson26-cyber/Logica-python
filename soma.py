import os

# Limpa o terminal.
os.system ("cls || clear")

numero = int(input("Digite um número para soma: "))

def somar_numero(numero):
    if numero == 0: 
        return 0
    else:
        print(f"{numero} + {numero -1}")
        return numero + somar_numero(numero - 1)

resultado = somar_numero(numero)
print(f"Soma de 0 até {numero}: {resultado}")