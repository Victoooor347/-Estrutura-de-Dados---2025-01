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
  
def imprimir_pre_ordem(root):
  print(root.chave)
  
  if root.esquerda is not None:
    imprimir_pre_ordem(root.esquerda)
  if root.direita is not None:
    imprimir_pre_ordem(root.direita)
  

# Montar estrutura da árvore 
arvore = BinaryTree()
valores = [5, 6, 7, 4, 2, 1, 3, 9, 8, 10]

for i in range(len(valores)):
  arvore.raiz = insert(arvore.raiz, valores[i])
  

imprimir_pre_ordem(arvore.raiz)