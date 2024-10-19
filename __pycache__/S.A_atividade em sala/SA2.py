fila = []
while True:
    print("""\nMenu de opções
1 - Adicionar um livro à fila
2 - Visualizar fila de livros
3 - Remover um livro da fila
4 - Sair do programa""")
   
    x = int(input("Digite a ação tomada: \n"))
    print("\n")
   
    if x == 1:
        y = input("\nDigite o livro que deseja adicionar à fila: ")
        fila.append(y)
   
    elif x == 2:
        if not fila:
            print("A fila de livros está vazia\n")
        else:
            for i, livro in enumerate(fila, start=1): #enumerate conta a quantidade de loops
                print(f"{i} - {livro}")
   
    elif x == 3:
        if not fila:
            print("A fila está vazia, não há livros para remover\n")
        else:
            y = input(f"O livro '{fila[0]}' será removido da fila. Confirmar (s/n)? ")
            if y.lower() == 's':#Lower converte maiusculo em minusculo
                removido = fila.pop(0)
                print(f"Livro '{removido}' removido da fila.")
            else:
                print("Remoção cancelada.")
   
    elif x == 4:
        print("Programa encerrado...")
        break
