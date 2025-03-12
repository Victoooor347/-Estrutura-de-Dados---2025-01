
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

def separa(lst, n):
    atual = lst
    segunda_lista = None
    anterior = None
    
    while atual is not None:
        if atual.info == n:
            if anterior is not None:
                anterior.prox = None  
            segunda_lista = atual.prox  
            break
        anterior = atual
        atual = atual.prox
    
    return lst, segunda_lista
            


lista_encadeada = Lista(11)

lista_encadeada = lista_insert(lista_encadeada, 4)
lista_encadeada = lista_insert(lista_encadeada, 3)
lista_encadeada = lista_insert(lista_encadeada, 9)
lista_encadeada = lista_insert(lista_encadeada, 7)
lista_encadeada = lista_insert(lista_encadeada, 5)
lista_encadeada = lista_insert(lista_encadeada, 3)

print("=-=-=-= Lista Atual =-=-=-=")
lista_imprime(lista_encadeada)

print("=== Separando listas ===")
lista1, lista2 = separa(lista_encadeada, 9)

print("=-=-=-= Primeira Lista =-=-=-=")
lista_imprime(lista1)

print("=-=-=-= Segunda Lista =-=-=-=")
lista_imprime(lista2)