# Inicializa a pilha com os elementos
pilha = [1, 1, 2, 3, 5]
print("Pilha inicial:", pilha)

# Adiciona elementos à pilha
def adicionar_elemento(pilha, elemento):
    pilha.append(elemento)
    print(f"Inserindo elemento {elemento}: {pilha}")

# Remove o último elemento da pilha
def remover_elemento(pilha):
    if pilha:  # Verifica se a pilha não está vazia
        elemento_removido = pilha.pop()
        print(f"Removendo elemento {elemento_removido}: {pilha}")
    else:
        print("A pilha está vazia, não há elementos para remover.")

# Adiciona elementos
adicionar_elemento(pilha, 8)
adicionar_elemento(pilha, 13)

# Remove elementos
remover_elemento(pilha)
remover_elemento(pilha)

def new_func():
    stack= []

    stack.append('a')
    stack.append('b')
    stack.append('c')

    print('Elementos inseridos na stack foram:')
    print(stack)

    print('Excluir elementos da stack:')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    print('Stack atual:')
    print(stack)

new_func()

lista = []
while True:
    print("""\nMenu de opções
1 - Adicionar um livro à lista
2 - Visualizar lista de livros
3 - Remover um livro da lista
4 - Sair do programa""")

    x = int(input("Digite a ação tomada:  \n"))
    print("\n")

    if x == 1:
        y = input("Digite o livro que deseja adicionar na lista: ")
        lista.append(y)
    elif x == 2:
        if lista:
            for i, livro in enumerate(lista, start=1):
                print(f"{i} - {livro}")
        else:
            print("A lista de livros está vazia\n")
    elif x == 3:
        if lista:
            for i, livro in enumerate(lista, start=1):
                print(f"{i} - {livro}")
            y = int(input("\nDigite o número do livro acima que deseja remover: "))
            lista.pop(y - 1)
        else:
            print("A lista de livros está vazia. Não é possível remover.\n")
    elif x == 4:
        print("Programa encerrado...")
        break
    else:
        print("Opção inválida. Tente novamente.")
