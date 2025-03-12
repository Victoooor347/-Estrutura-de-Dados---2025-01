
class Lista:
    def __init__(self, value):
        self.info = value
        self.prox = None

def lista_insert(primeiro_elemento, valor):
    novo_elemento = Lista(valor)
    novo_elemento.prox = primeiro_elemento

    return novo_elemento

def lista_imprime(lista):
    atual = lista

    while atual is not None:
        print(atual.info)
        atual = atual.prox


lista_encadeada = Lista(11)

lista_encadeada = lista_insert(lista_encadeada, 9)
lista_encadeada = lista_insert(lista_encadeada, 7)
lista_encadeada = lista_insert(lista_encadeada, 5)
lista_encadeada = lista_insert(lista_encadeada, 3)

print("=-=-=-= Lista Atual =-=-=-=")
lista_imprime(lista_encadeada)