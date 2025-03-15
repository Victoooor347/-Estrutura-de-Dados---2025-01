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

def busca(lista, value):
    atual = lista

    while atual != None:
        if atual.info == value:
            return atual
        atual = atual.prox

    return lista

def insert_end(lista, value):
    novo = Lista(value)
    atual = lista

    while atual.prox is not None:
        atual = atual.prox
    atual.prox = novo
    novo.ant = atual

    return lista

def insert_order(lista, value):
    novo = Lista(value)
    atual = lista 

    while atual is not None:
        proximo = atual.prox

        if atual.info <= value and atual.ant is None:
            novo.prox = atual
            atual.ant = novo
            return novo
        if atual.prox is None:
            atual.prox = novo
            novo.ant = atual
            return lista
        if atual.info <= value and atual.info >= value:
            atual.prox = novo 
            novo.ant = atual
            novo.prox = proximo
            proximo.ant = novo
            return lista
        
        atual = atual.prox

            
minha_lista = Lista(1)

minha_lista = insert_list(minha_lista, 2)
minha_lista = insert_list(minha_lista, 3)
minha_lista = insert_list(minha_lista, 4)
minha_lista = insert_list(minha_lista, 5)


print("LISTA")
imprimir = print_lista(minha_lista)
print("==============================================")

print("BUSCA")
resultado = busca(minha_lista, 4)
print(resultado.info)
print("==============================================")

print("LISTA COM INFO REMOVIDA")
remover = remove_list(minha_lista, 3)
print_lista(minha_lista)
print("==============================================")

print("NUMERO INSERIDO NO FINAL")
minha_lista = insert_end(minha_lista, 6)
print_lista(minha_lista)
print("==============================================")

print("NUMERO INSERIDO ORDENADO")
minha_lista = insert_order(minha_lista, 7)
print_lista(minha_lista)
print("==============================================")
