
class ListaNode:
    def __init__(self, info):
        self.info = info
        self.prox = None

class Pilha:
    def __init__(self, capacidade, topo = None):
        self.topo = topo
        self.capacidade = capacidade
        self.num_elementos = 0


def pilha_push(pilha, valor):
    if pilha.num_elementos >= pilha.capacidade:
        print("Capacidade máxima alcançada!")
        return

    if pilha.topo == None:
        pilha.num_elementos += 1
        elemento = ListaNode(valor)
        pilha.topo = elemento

        return pilha

    pilha.num_elementos += 1
    elemento = ListaNode(valor)
    elemento.prox = pilha.topo
    pilha.topo = elemento

    return pilha

def pilha_show(pilha):
    atual = pilha.topo

    while atual != None:
        print(atual.info)
        atual = atual.prox

def pilha_pop(pilha):
    if pilha.topo == None:
        print("Pilha vazia!")
    else:
        pilha.topo = pilha.topo.prox
        pilha.num_elementos -= 1

def pilha_vazia(pilha):
    return pilha.topo == None

pilha = Pilha(3)

pilha_push(pilha, 1)
pilha_push(pilha, 2)
pilha_push(pilha, 3)
pilha_push(pilha, 4)
pilha_push(pilha, 5)

print("=-=-=-=-=-=-=--=-=-=")
pilha_show(pilha)

pilha_pop(pilha)
pilha_pop(pilha)
pilha_pop(pilha)
pilha_pop(pilha)
pilha_pop(pilha)
pilha_pop(pilha)

print("=-=-=-=-=-=-=--=-=-=")
pilha_show(pilha)