
# class Lista:
#     def __init__(self):
#         print("instanciou")

# minha_lista = Lista()          //chama e executa a class



class Lista:
    def __init__(self, info):
        self.info = info
        self.prox = None

def insert_node(lista, value):
    atual = lista

    while atual.prox != None:
        atual = atual.prox

    novo_item = Lista(value)
    atual.prox = novo_item


def print_lista(lista):
    atual = lista

    while atual != None:
        print(atual.info)
        atual = atual.prox


def search_list(lista, value):
    atual = lista

    while atual != None:
        if atual.info == value:
            return atual
        atual = atual.prox

    return atual #ou return None

def remove_list(lista, value):
    atual = lista
    anterior = None

    while atual is not None:
        if atual.info == value:
            if atual == lista:
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

insert_node(minha_lista, 2)
insert_node(minha_lista, 3)


print(minha_lista.info)
print(minha_lista.prox.info)
print(minha_lista.prox.prox.info)

print(search_list(minha_lista, 4))
print("=====================================")


print_lista(minha_lista)

print("=====================================")
minha_lista = remove_list(minha_lista, 2)

print_lista(minha_lista)
