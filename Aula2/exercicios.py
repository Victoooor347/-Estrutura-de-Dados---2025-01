
class Lista:
    def __init__(self, value):
        self.info = value
        self.prox = None

def inserir(primeiro_elemento, valor):
    novo_elemento = Lista(valor)
    primeiro_elemento = novo_elemento

    return primeiro_elemento

def mostrar(lista):

    atual = lista
    
    if atual is not None:
        print(atual.info)
        atual = atual.prox

lista_encadeada = Lista(1)

lista_encadeada = inserir(lista_encadeada, 2)

print("lista")
mostrar(lista_encadeada)