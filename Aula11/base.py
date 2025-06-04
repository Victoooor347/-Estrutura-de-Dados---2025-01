class Nodo:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return '%s <- %s -> %s' % (
            self.esquerda and self.esquerda.chave,
            self.chave,
            self.direita and self.direita.chave
        )

class BinaryTree:
    def __init__(self):
        self.raiz = None

def insert(root, key):
    if root is None:
        return Nodo(key)
    if key < root.chave:
        root.esquerda = insert(root.esquerda, key)
    else:
        root.direita = insert(root.direita, key)
    return root


arvore = BinaryTree()
valores = [5, 6, 7, 4, 2, 1, 3, 9, 8, 10]

for i in range(len(valores)):
    arvore.raiz = insert(arvore.raiz, valores[i])