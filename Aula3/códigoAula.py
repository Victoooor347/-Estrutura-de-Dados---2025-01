
# def insert_order(lista, value):
#     atual = lista
#     novo = Lista(value)
#
#     while atual is not None:
#         print("Uma execução")
#         # Primeiro elemento
#         if atual.ant is None and value < atual.info:
#             novo.prox = atual
#             atual.ant = novo
#             return novo
#         # Insere no Final
#         if atual.prox is None:
#             novo.ant = atual
#             atual.prox = novo
#             return lista
#         if value >= atual.info and value <= atual.prox.info:
#             proximo = atual.prox
#
#             # Atualiza dados de ligação "Antes"
#             atual.prox = novo
#             novo.ant = atual
#             # Atualiza dados de ligação "Depois"
#
#             proximo.ant = novo
#             novo.prox = proximo
#             return lista
#
#         print("Definiu anterior")
#         atual = atual.prox
#
#     return lista

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

def print_list(lista):
    atual = lista

    while atual is not None:
        print(atual.info)
        atual = atual.prox

def remove_list(lista, value):
    atual = lista
    anterior = None

    while atual is not None:
        if atual.info == value:
            if atual == lista:
                if atual.prox is not None:
                    proximo = atual.prox
                    proximo.ant = None
                return atual.prox
            elif atual.prox == None:
                anterior.prox = None
                return lista
            else:
                anterior.prox = atual.prox

                if atual.prox is not None:
                    proximo = atual.prox
                    proximo.ant = anterior

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

def insert_order(lista, value):
    atual = lista
    novo = Lista(value)

    while atual is not None:
        proximo = atual.prox

        # Regra para inserir no início - Caso o valor seja o primeiro
        if value <= atual.info and atual.ant is None:
            novo.prox = atual
            atual.ant = novo
            return novo
        # Regra para inserir no final - Caso valor seja o último
        if atual.prox is None:
            atual.prox = novo
            novo.ant = atual
            return lista
        if value >= atual.info and value <= proximo.info:
            # Faz conexão <-
            atual.prox = novo
            novo.ant = atual
            # Faz conexão ->
            novo.prox = proximo
            proximo.anterior = novo
            return lista



        atual = atual.prox

minha_lista = Lista(7)
minha_lista = insert_list(minha_lista, 5)
minha_lista = insert_list(minha_lista, 3)

print_list(minha_lista)
print("=-=-=-=-=-=-=-=")

minha_lista = insert_order(minha_lista, 4)
print_list(minha_lista)
print("=-=-=-=-=-=-=-=")

minha_lista = print_inverse(minha_lista)
print_list(minha_lista)