import os

# Limpa o terminal.
os.system("cls" if os.name == "nt" else "clear")

a = 10
b = 20

auxiliar = a 

a = b 
b = auxiliar
# Troca valores de lugar. 
print(f"a = {a}")
print(f"b = {b} ")

a = 70 
b = 140
# Vai modificar a posição dos valores, a indo para b. 
auxiliar = a 

a = b 

b = auxiliar

print (f"a = {a}")
print (f"b= {b}")
