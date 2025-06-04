class Nodo:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

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
  
def count_pair(raiz):
  if raiz is None:
    return 0
  
  if raiz.chave % 2 == 0:
    return count_pair(raiz.esquerda) + count_pair(raiz.direita) + 1
  return count_pair(raiz.esquerda) + count_pair(raiz.direita)

# Montar estrutura da árvore 
arvore = BinaryTree()
valores = [5, 6, 7, 4, 2, 1, 3, 9, 8, 10]

for i in range(len(valores)):
  arvore.raiz = insert(arvore.raiz, valores[i])
  
print(count_pair(arvore.raiz))
