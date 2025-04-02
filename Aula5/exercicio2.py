
class Pilha:
    def __init__(self, cap):
        self.cap = cap
        self.n = 0
        self.vet = []

def pilha_push(pilha, value):
    if pilha.n == None:
        print("cheia")
        return pilha

    pilha.vet.append(value)

    if pilha.n == pilha.cap - 1:
        pilha.n = None
    else:
        pilha.n += 1

def esvaziar_pilha(pilha):
    if pilha.n == 0:
        print("pilha vazia")

    while True:
        valor = pilha.vet.pop()
        print(f"valor {valor} removido")
        
        if pilha.n == None:
            pilha.n = pilha.cap - 1
        else:
            pilha.n -= 1
        if pilha.n == 0:
            print("pilha esvaziada")
            break

pilha = Pilha(5)

pilha_push(pilha, 1)
pilha_push(pilha, 2)
pilha_push(pilha, 3)
pilha_push(pilha, 4)
pilha_push(pilha, 5)

print(pilha.vet)
print(pilha.n)
print("=====================")
esvaziar_pilha(pilha)
