
class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

def insert_node(lista, info):
    new_element = Lista(info)

    if lista == None:
        new_element.prox = new_element
        return new_element

    atual = lista

    while atual.prox != lista:
        atual = atual.prox

    atual.prox = new_element
    new_element.prox = lista

    return new_element

def show_elements(lista):
    atual = lista

    while True:
        print(atual.info)
        atual = atual.prox

        if atual == lista:
            break

def remove_element(lista, value):
    if lista.prox == lista:
        if lista.info == value:
            print("Esvaziando lista...")
            return None

        print("Item não localizado!")
        return lista

    if lista.info == value:
        ultimo_elemento = lista

        # Ir até o final da lista -> Atual = Último elemento da lista
        while ultimo_elemento.prox != lista:
            ultimo_elemento = ultimo_elemento.prox

        ultimo_elemento.prox = lista.prox

        return lista.prox

    atual = lista
    anterior = None

    while True:
        if atual.info == value:
            anterior.prox = atual.prox

        anterior = atual
        atual = atual.prox

        if atual == lista:
            print("Item não localizado!")
            break

    return lista

lista = None

lista = insert_node(lista, 9)
lista = insert_node(lista, 7)
lista = insert_node(lista, 5)
lista = insert_node(lista, 3)

lista = remove_element(lista, 5)
show_elements(lista)