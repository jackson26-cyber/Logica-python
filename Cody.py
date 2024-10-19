# Comandos de Controle de Fluxo
if / elif / else: Controlam o fluxo condicional do programa.


if condição:
    # código se a condição for verdadeira
elif outra_condição:
    # código se a outra condição for verdadeira
else:
    # código se nenhuma condição for verdadeira
for: Laço de repetição que itera sobre sequências (listas, strings, dicionários, etc.).


for elemento in lista:
    # código que será executado para cada elemento
while: Executa um bloco de código enquanto a condição for verdadeira.


while condição:
    # código enquanto a condição for verdadeira

break: Encerra um laço antecipadamente.


for i in range(10):
    if i == 5:
        break  # interrompe o laço quando i for 5
continue: Pula a iteração atual e vai para a próxima no laço.


for i in range(10):
    if i == 5:
        continue  # pula o restante do código quando i for 5
pass: Usado como um placeholder para código que será implementado mais tarde.


if condição:
    pass  # nada acontece, usado como placeholder
 
 #Comandos de Funções e Classes
def: Define uma função.


def minha_funcao():
    print("Olá, mundo!")
return: Retorna um valor de uma função.


def soma(a, b):
    return a + b
class: Define uma classe (usado em programação orientada a objetos).


class MinhaClasse:
    def __init__(self, valor):
        self.valor = valor

#Comandos de Manipulação de Dados
print(): Exibe informações no console.


print("Olá, mundo!")
input(): Recebe uma entrada do usuário.


nome = input("Qual é o seu nome?")
len(): Retorna o comprimento (número de itens) de uma lista, string ou outra estrutura.


comprimento = len([1, 2, 3])
type(): Retorna o tipo de um objeto.


tipo = type(42)  # retorna <class 'int'>
range(): Gera uma sequência de números, útil para laços.


for i in range(5):
    print(i)  # imprime de 0 a 4
str() / int() / float(): Converte um valor para uma string, inteiro ou número de ponto flutuante, respectivamente.


numero_str = str(42)  # converte o número para string
sum(): Soma todos os itens em uma lista ou sequência numérica.


total = sum([1, 2, 3, 4])
max() / min(): Retorna o maior ou menor valor de uma sequência.


maior_valor = max([1, 5, 3])
sorted(): Retorna uma lista ordenada dos itens.


lista_ordenada = sorted([3, 1, 2])

#Comandos de Estruturas de Dados
Listas:
append(): Adiciona um item no final da lista.


lista = [1, 2, 3]
lista.append(4)
remove(): Remove o primeiro item correspondente ao valor especificado.


lista.remove(2)
pop(): Remove e retorna o último item da lista, ou o item no índice especificado.


item = lista.pop()  # remove o último item
extend(): Adiciona todos os itens de outra lista à lista atual.


lista.extend([4, 5])
Dicionários:
keys(): Retorna uma lista com as chaves do dicionário.


dicionario = {'chave1': 'valor1', 'chave2': 'valor2'}
chaves = dicionario.keys()
values(): Retorna uma lista com os valores do dicionário.


valores = dicionario.values()
items(): Retorna uma lista de tuplas contendo pares de chave e valor.


itens = dicionario.items()
get(): Retorna o valor para uma chave específica. Se a chave não existir, retorna um valor padrão.


valor = dicionario.get('chave1', 'valor_padrão')
#Comandos de Manipulação de Arquivos
open(): Abre um arquivo para leitura ou escrita.


arquivo = open('arquivo.txt', 'r')  # modo de leitura
read(): Lê o conteúdo do arquivo.


conteudo = arquivo.read()
write(): Escreve no arquivo (usado em modo de escrita 'w' ou modo de adição 'a').


arquivo = open('arquivo.txt', 'w')
arquivo.write("Escrevendo no arquivo")
close(): Fecha o arquivo.


arquivo.close()

#Comandos de Exceções
try / except: Trata exceções ou erros no código.


try:
    # código que pode gerar um erro
    x = 1 / 0
except ZeroDivisionError:
    print("Divisão por zero não é permitida")
finally: Um bloco que é sempre executado, mesmo que uma exceção tenha ocorrido.


try:
    x = 1 / 0
except ZeroDivisionError:
    print("Erro!")
finally:
    print("Sempre será executado.")

#Comandos de Módulos e Importações
import: Importa um módulo (biblioteca externa ou interna) para o código.


import math
from: Importa funções específicas de um módulo.


from math import sqrt
as: Usado para dar um alias (nome alternativo) a um módulo.


import numpy as np
# Funções Integradas Úteis (Built-in Functions)
map(): Aplica uma função a todos os itens de uma lista.


lista = [1, 2, 3]
nova_lista = list(map(lambda x: x * 2, lista))
filter(): Filtra os itens de uma lista com base em uma condição.


lista = [1, 2, 3, 4]
pares = list(filter(lambda x: x % 2 == 0, lista))
zip(): Combina duas listas em uma lista de tuplas.


lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
combinada = list(zip(lista1, lista2))