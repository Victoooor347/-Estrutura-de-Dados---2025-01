
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

def pilha_top(pilha):
    if pilha.n == None:
        return pilha.cap - 1
    
    if pilha.n == 0:
        return None
    
    return pilha.n -1



pilha = Pilha(5)

pilha_push(pilha, 1)
pilha_push(pilha, 2)
pilha_push(pilha, 3)
pilha_push(pilha, 4)
pilha_push(pilha, 5)

print(pilha.vet)
print(pilha.n)

ultimo = pilha_top(pilha)
print(ultimo)
