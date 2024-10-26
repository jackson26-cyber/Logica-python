import os
import time
# Limpa o terminal.
os.system("cls || clear")

# Função.
def contagem_regressiva(numero):
    if numero < 0:
        return
    print(numero)
    time.sleep(10) # time.sleep é o tempo decorrido para ele chamar o proximo comando, nesse caso 10s 
    contagem_regressiva(numero -1) # chamada recursiva. Vaichamar o numeral a partir do que for adicionado dentro dos () e reduzindo -1
print("Contagem regressiva...")# Chama na tela, a parte escrita "contagem regressiva"
contagem_regressiva(20)  # Chamada da função.
print("===FIM===") 
