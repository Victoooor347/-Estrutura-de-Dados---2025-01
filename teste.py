class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pares(arv):
    if arv is None:
        return 0

    # Verifica se o valor do nó atual é par
    if arv.data % 2 == 0:
        return 1 + pares(arv.left) + pares(arv.right)
    else:
        return pares(arv.left) + pares(arv.right)

# Exemplo de uso:

# Construindo a seguinte árvore:
#        10
#       /  \
#      5    4
#          / \
#         2   7

raiz = BinaryTree(10)
raiz.left = BinaryTree(5)
raiz.right = BinaryTree(4)
raiz.right.left = BinaryTree(2)
raiz.right.right = BinaryTree(7)

# Chamando a função
print("Quantidade de nós com valores pares:", pares(raiz))
