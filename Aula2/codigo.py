
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

def lista_busca(lista, valor):
    atual = lista

    while atual is not None:
        if atual.info == valor:
            return atual
        atual = atual.prox

    return None

def lista_remove(lista, valor):
    atual = lista
    anterior = None

    while atual is not None:
        if atual.info == valor:
            if anterior == None:
                return atual.prox
            elif atual.prox == None:
                anterior.prox = None
                return lista
            else:
                anterior.prox = atual.prox
                return lista

        anterior = atual
        atual = atual.prox

    return lista

def lista_imprime_recursivo(lista):
    print(lista.info)

    if lista.prox != None:              
        lista_imprime_recursivo(lista.prox)



lista_encadeada = Lista(11)

lista_encadeada = lista_insert(lista_encadeada, 9)
lista_encadeada = lista_insert(lista_encadeada, 7)
lista_encadeada = lista_insert(lista_encadeada, 5)
lista_encadeada = lista_insert(lista_encadeada, 3)

# print("=-=-=-= Lista Atual =-=-=-=")
# lista_imprime(lista_encadeada)
#
# lista_encadeada = lista_remove(lista_encadeada, 7)
#
# print("=-=-=-= Lista Atualizada =-=-=-=")
# lista_imprime(lista_encadeada)

lista_imprime_recursivo(lista_encadeada)