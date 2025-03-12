
class Lista:
    def __init__(self, info):
        self.info = info
        self.ant = None
        self.prox = None

def insert_list(lista, value):
    novo_elemento = Lista(value)

    novo_elemento.prox = lista
    lista.ant = novo_elemento

    return novo_elemento


def print_lista(lista):
    atual = lista

    while atual != None:
        print(atual.info)
        atual = atual.prox

def remove_list(lista, value):
    atual = lista
    anterior = None

    while atual is not None:
        if atual.info == value:
            if atual == lista:
                prox = atual.prox
                prox.ant = None
                return atual.prox
            elif atual.prox == None:
                anterior.prox = None
                return lista
            else:
                anterior.prox = atual.prox
                return lista
            

        anterior = atual
        atual = atual.prox



minha_lista = Lista(1)

minha_lista = insert_list(minha_lista, 5)
minha_lista = insert_list(minha_lista, 8)
minha_lista = insert_list(minha_lista, 7)
minha_lista = insert_list(minha_lista, 9)
print_lista(minha_lista)

print("=========================")


minha_lista = remove_list(minha_lista, 8)

print_lista(minha_lista)