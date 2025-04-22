
class Node:
    def __init__(self, info):
        self.info = info
        self.prox = None

class Pilha:
    def __init__(self, capacidade = 10, topo = None, ):
        self.topo = topo
        self.capacidade = capacidade
        self.num_elementos = 0

def pilha_push(pilha, valor):
    if pilha.num_elementos >= pilha.capacidade:
        print("capacidade maxima alcançada")
        return pilha
    
    if pilha.topo == None:
        pilha.num_elementos += 1
        novo = Node(valor)
        pilha.topo = novo

        return pilha
    
    pilha.num_elementos += 1
    novo = Node(valor)
    novo.prox = pilha.topo
    pilha.topo = novo

    return pilha

def mostrar_pilha(pilha):
    atual = pilha.topo

    while atual != None:
        print(atual.info)
        atual = atual.prox

def desempilhar(pilha):
    atual = pilha.topo

    while atual != None:
        print(atual.info)
        atual = atual.prox
        pilha.num_elementos -= 1

    
pilha = Pilha(10)

pilha_push(pilha, 1)
pilha_push(pilha, 2)
pilha_push(pilha, 3)
pilha_push(pilha, 4)
pilha_push(pilha, 5)

mostrar_pilha(pilha)

print("=====================================")

desempilhar(pilha)
 

 