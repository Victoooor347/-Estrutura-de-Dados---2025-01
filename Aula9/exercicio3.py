
class No:
    def __init__(self, chave = None, direita = None, esquerda = None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (
            self.esquerda and self.esquerda.chave,
            self.chave,
            self.direita and self.direita.chave
        )

def insert(root, key):
    if root == None:
        return No(key)
    if key < root.chave:
        root.esquerda = insert(root.esquerda, key)
    else:
        root.direita = insert(root.direita, key)
    return root


raiz = No(3)
raiz.esquerda = No(5)
raiz.direita = No(1)

print("Árvore: ", raiz)
print("======================================")

insert(raiz, 7)
print("Árvore: ", raiz)

