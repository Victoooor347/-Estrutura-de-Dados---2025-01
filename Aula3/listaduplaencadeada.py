
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
                if atual.prox is not None:
                    prox = atual.prox
                    prox.ant = None
                return atual.prox
            elif atual.prox == None:
                anterior.prox = None
                return lista
            else:
                anterior.prox = atual.prox
                if atual.prox is not None:
                    prox = atual.prox
                    prox.ant = anterior
                return lista
            

        anterior = atual
        atual = atual.prox


def get_last_element(lista):
    atual = lista

    while atual.prox is not None:
        atual = atual.prox

    return atual


def print_inverse(ultimo_elemento):
    atual = ultimo_elemento

    while atual is not None:
        print(atual.info)
        atual = atual.ant


def insert_end(lista, value):
    novo = Lista(value)
    atual = lista

    while atual is not None:
        if atual.prox == None:
            atual.prox = novo
            novo.ant = atual

    return lista


def insert_order(lista, value):
    novo = Lista(value)
    atual = lista
    anterior = None











minha_lista = Lista(1)

minha_lista = insert_list(minha_lista, 5)
minha_lista = insert_list(minha_lista, 8)
minha_lista = insert_list(minha_lista, 7)
minha_lista = insert_list(minha_lista, 9)
print_lista(minha_lista)

print("=========================")

minha_lista = remove_list(minha_lista, 8)
print_lista(minha_lista)

print("=========================")

# ultimo_elemento = get_last_element(minha_lista)
# print(ultimo_elemento.info)

print("=========================")

inverso = print_inverse(minha_lista)
print(inverso)