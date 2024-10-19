import os

# Limpa o terminal.
os.system("cls" if os.name == "nt" else "clear")

# Funções.
def calcular_somar(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

def calcular_subtracao(primeiro_numero, segundo_numero):
    return primeiro_numero - segundo_numero

# Entrada.
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

# Processamento.
soma = calcular_somar(primeiro_numero, segundo_numero)
subtracao = calcular_subtracao(primeiro_numero, segundo_numero)

# Saída.
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
