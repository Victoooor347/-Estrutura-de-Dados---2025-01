
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

def copia(lst):
    
    copia_lista = Lista(lst.info)
    atual_original = lst.prox
    atual_copia = copia_lista


    while atual_original is not None:
        novo = Lista(atual_original.info) 
        atual_copia.prox = novo  
        atual_copia = novo  
        atual_original = atual_original.prox  
    
    return copia_lista 

lista1 = Lista("C")
lista1 = lista_insert(lista1, "B")
lista1 = lista_insert(lista1, "A")

lista2 = copia(lista1)

print("Lista original:")
lista_imprime(lista1)  

print("Lista copiada:")
lista_imprime(lista2)