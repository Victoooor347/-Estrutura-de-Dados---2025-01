
class Pilha:
    def __init__(self, cap):
        self.cap = cap
        self.n = 0
        self.vet = []

def push(pilha, valor):
    if pilha.n == None:
        print("pilha cheia")
        return pilha
    
    pilha.vet.append(valor)

    if pilha.n == pilha.cap - 1:
        pilha.n = None
    else:
        pilha.n += 1

def desempilhar(pilha):
    while True:
        if pilha.n == 0:
            print("pilha vazia")
            break

        valor = pilha.vet.pop()
        print(valor)

        if pilha.n == None:
            pilha.n = pilha.cap - 1
        else:
            pilha.n -= 1
        
        if pilha.n == 0:
            break
        

pilha = Pilha(10)

push(pilha, 1)
push(pilha, 2)
push(pilha, 3)
push(pilha, 4)
push(pilha, 5)

print(pilha.vet)

print("==============================")

desempilhar(pilha)