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

def contar_elementos(lista):
    atual = lista
    cont = 0 

    while True:
        cont += 1
        atual = atual.prox

        if atual == lista:
            break
        
    return cont
        
lista = None

lista = insert_node(lista, 9)
lista = insert_node(lista, 7)
lista = insert_node(lista, 5)
lista = insert_node(lista, 3)

print("=-=-=-= ANTES =-=-=-=")
show_elements(lista)

print("=================")
quantidade = contar_elementos(lista)
print(f"a quantidade de elementos é {quantidade}")
