# # Exibir os dados.
# print (notas [0])
# print (notas [1])
# print (notas [2])

vetor_notas= []
for i in range (3):
    nota= float(input("Digite uma nota: "))
    vetor_notas.append(nota)

    #For Each
    for cada_nota in vetor_notas:
        print(cada_nota)