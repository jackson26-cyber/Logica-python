# Cria uma fila com três elementos. 
fila = [" Banana", "Maçã", "Pera"]
print ("Fila: ", fila)

# Adiciona um elemento ao final da fila. 
fila.append ("Uva")
print ("Adicionando um elemento: ", fila)

# Remove o primeiro elemento adicionado à fila.
fila.pop(0)
print("Removendo um elemento: ", fila)

fila =[]

# Adicionando elementos na fila a partir da entrada do usuário
for i in range (3):
    num =int(input("Digite um número"))
    fila.append(num)
print(fila) #Saída:[num1,num2,num3]

# Removendo o elemento mais antigo da fila
primeiro_elemento= fila.pop(0)
print(primeiro_elemento) #Saída:num1
print(fila) #Saída:[num2,num3]

fila = []

# Adicionando elementos na fila a partir da entrada do usuário
for i in range (3):
    texto = input("Digite uma string: ")
    fila.append(texto)
print(fila) #Saída: [str1, str2, str3]

# Removendo o elemento mais antigo da fila
primeiro_elemento = fila.pop(0)
print (primeiro_elemento) #Saída: str1
print (fila) #Saída: [str2, str3]