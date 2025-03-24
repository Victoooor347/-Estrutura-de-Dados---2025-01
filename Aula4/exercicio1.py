
class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

def insert(lista, value):
    novo = Lista(value)

    if lista == None:
        novo.prox = novo 
        return novo

    atual = lista

    while atual.prox != lista:
        atual = atual.prox

    atual.prox = novo
    novo.prox = lista

    return novo

def show_elements(lista):
    atual = lista

    while True:
        print(atual.info)
        atual = atual.prox

        if atual == lista:
            break


def insert_end(lista, value):
    ultimo = Lista(value)
    atual = lista

    if atual is None:
        atual = ultimo
        return ultimo

    while atual.prox != lista:
        atual = atual.prox

    atual.prox = ultimo
    ultimo.prox = lista

    return lista
    

lista = None

lista = insert(lista, 1)
lista = insert(lista, 2)
lista = insert(lista, 3)
lista = insert(lista, 4)


show_elements(lista)

print("================")

lista = insert_end(lista, 5)
show_elements(lista)