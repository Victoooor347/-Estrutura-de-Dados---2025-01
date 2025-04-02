
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

def pilha_pop(pilha):
    if pilha.n == 0:
        print("")
        return None
    
    valor = pilha.vet.pop()

    if pilha.n == None:
        pilha.n = pilha.cap - 1
    else:
        pilha.n -= 1
    
    return valor

def pilha_top(pilha):
    if pilha.n == None:
        return pilha.cap - 1
    
    if pilha.n == 0:
        return None
    
    return pilha.n -1

def novo_push(pilha):
    for i in range(5):
        num = int(input("digite 5 numeros: "))
        pilha_push(pilha, num)
    
    print(pilha.vet)

    for i in range(5):
        valor = pilha_pop(pilha)
        print(valor)

pilha = Pilha(5)

# print(pilha.vet)
# print(pilha.n)
# print("===============================")
# ultimo = pilha_top(pilha)
# print(ultimo)
print("=============================")
novo_push(pilha)