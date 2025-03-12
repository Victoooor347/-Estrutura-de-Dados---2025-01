
class Lista1:
    def __init__(self, value):
        self.info = value
        self.prox = None

class Lista2:
    def __init__(self, value):
        self.info = value
        self.prox = None

def lista_insert1(primeiro_elemento, valor):
    novo_elemento = Lista1(valor)
    novo_elemento.prox = primeiro_elemento

    return novo_elemento


def lista_insert2(primeiro_elemento, valor):
    novo_elemento = Lista2(valor)
    novo_elemento.prox = primeiro_elemento

    return novo_elemento

def lista_imprime(lista1):
    atual = lista1

    while atual is not None:
        print(atual.info)
        atual = atual.prox

def merge(l1, l2):
    lista1 = l1
    lista2 = l2
    juntar = None

    if lista1.info == None:
        juntar = Lista2
    else:
        juntar = lista1
    
    if juntar == None:
        juntar = lista1.info
        juntar = lista2.info

    return juntar


lista_encadeada1 = Lista1(11)

lista_encadeada1 = lista_insert1(lista_encadeada1, 9)
lista_encadeada1 = lista_insert1(lista_encadeada1, 7)

lista_encadeada2 = Lista2(10)
lista_encadeada2 = lista_insert2(lista_encadeada2, 3)
lista_encadeada2 = lista_insert2(lista_encadeada2, 5)

print("=-=-=-= Lista Atual 1 =-=-=-=")
lista_imprime(lista_encadeada1)

print("=-=-=-= Lista Atual 2 =-=-=-=")
lista_imprime(lista_encadeada2)

# print("=-=-=-= Listas Juntas =-=-=-=")
# lista_imprime()