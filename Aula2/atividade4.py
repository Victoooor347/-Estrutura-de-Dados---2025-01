
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
        print(atual.info, end=" -> ")
        atual = atual.prox
    print("None")

def inverte(lst):
    anterior = None
    atual = lst
    while atual is not None:
        proximo = atual.prox
        atual.prox = anterior
        anterior = atual
        atual = proximo
    return anterior

minha_lista = Lista(2.1)
minha_lista = lista_insert(minha_lista, 4.5)
minha_lista = lista_insert(minha_lista, 1.0)
minha_lista = lista_insert(minha_lista, 7.2)
minha_lista = lista_insert(minha_lista, 9.8)

print("Lista Original:")
lista_imprime(minha_lista)

lista_invertida = inverte(minha_lista)

print("Lista Invertida:")
lista_imprime(lista_invertida)