import random

atrizes= ["Adriana Prado", "Bárbara Borges", "Camila Queiroz","Danielle Winits", "Fernanda Paes Leme", "helena Ranaldi", "Paolla de Oliveira", "Raquel Nunes", "Viola Davis"]

#Embaralha elementos
random.shuffle(atrizes)

# Ordena elementos crescentemente
atrizes.sort()#mesmo que usar atrizes.sort(reverse= Fales)
print(atrizes)

# Ordena elementos decrescentemente
atrizes.sort(reverse= True)
print(atrizes)