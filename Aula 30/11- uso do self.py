#Uma Classe Pessoa que tem nome e idade, e um método para apresentar a pessoa.

class pessoa: 
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, eu sou {self.nome} e tenho {self.idade} anos"
    
p1 = pessoa ("joão", 25)
p2 = pessoa ("Maria", 30)

print(p1.apresentar())
print(p2.apresentar())