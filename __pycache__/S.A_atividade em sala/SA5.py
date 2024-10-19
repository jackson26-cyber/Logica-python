class Pilha:
    def __init__(self):
        # Inicializa a pilha com um tamanho máximo de 20 e uma lista vazia
        self.max_tamanho = 20
        self.elementos = []
    
    def empilhar(self, elemento):
        """Adiciona um elemento no topo da pilha."""
        if len(self.elementos) < self.max_tamanho:
            self.elementos.append(elemento)  # Adiciona o elemento
        else:
            print("Pilha cheia! Não é possível empilhar mais elementos.")
    
    def desempilhar(self):
        """Remove e retorna o elemento do topo da pilha."""
        if not self.vazia():
            return self.elementos.pop()  # Remove e retorna o último elemento
        else:
            print("Pilha vazia! Não é possível desempilhar.")
            return None
    
    def limpar(self):
        """Remove todos os elementos da pilha."""
        self.elementos.clear()  # Limpa a lista de elementos
    
    def listar(self):
        """Lista todos os elementos armazenados na pilha."""
        return self.elementos  # Retorna a lista de elementos
    
    def vazia(self):
        """Verifica se a pilha está vazia."""
        return len(self.elementos) == 0  # Retorna True se não houver elementos

