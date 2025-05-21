class Nodo:
    def _init_(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def _repr_(self):
        return '%s <- %s -> %s' % (
            self.esquerda and self.esquerda.chave,
            self.chave,
            self.direita and self.direita.chave
        )

class BinaryTree:
    def _init_(self):
        self.raiz = None

    def inserir(self, chave):
        self.raiz = self._inserir(self.raiz, chave)

    def _inserir(self, node, chave):
        if node is None:
            return Nodo(chave)
        if chave < node.chave:
            node.esquerda = self._inserir(node.esquerda, chave)
        else:
            node.direita = self._inserir(node.direita, chave)
        return node

    def buscar(self, chave):
        return self._buscar(self.raiz, chave)

    def _buscar(self, node, chave):
        if node is None or node.chave == chave:
            return node
        if chave < node.chave:
            return self._buscar(node.esquerda, chave)
        else:
            return self._buscar(node.direita, chave)

    def remover(self, chave):
        self.raiz = self._remover(self.raiz, chave)

    def _remover(self, node, chave):
        if node is None:
            return None

        if chave < node.chave:
            node.esquerda = self._remover(node.esquerda, chave)
        elif chave > node.chave:
            node.direita = self._remover(node.direita, chave)
        else:
            if node.esquerda is None and node.direita is None:
                return None
            elif node.esquerda is None:
                return node.direita
            elif node.direita is None:
                return node.esquerda
            else:
                temp = node.esquerda
                while temp.direita is not None:
                    temp = temp.direita
                node.chave = temp.chave
                node.esquerda = self._remover(node.esquerda, temp.chave)
        return node

    def pre_ordem(self):
        self._pre_ordem(self.raiz)
        print()

    def _pre_ordem(self, node):
        if node:
            print(node.chave, end=' ')
            self._pre_ordem(node.esquerda)
            self._pre_ordem(node.direita)

    def em_ordem(self):
        self._em_ordem(self.raiz)
        print()

    def _em_ordem(self, node):
        if node:
            self._em_ordem(node.esquerda)
            print(node.chave, end=' ')
            self._em_ordem(node.direita)

    def pos_ordem(self):
        self._pos_ordem(self.raiz)
        print()

    def _pos_ordem(self, node):
        if node:
            self._pos_ordem(node.esquerda)
            self._pos_ordem(node.direita)
            print(node.chave, end=' ')

arvore = BinaryTree()

for valor in [6, 2, 1, 4, 3, 8]:
    arvore.inserir(valor)

print("Árvore em ordem simétrica:")
arvore.em_ordem()

print("Árvore em pré-ordem:")
arvore.pre_ordem()

print("Árvore em pós-ordem:")
arvore.pos_ordem()

print("\nBusca pelo elemento 4:")
nodo_encontrado = arvore.buscar(4)
print("Encontrado:", nodo_encontrado)

print("\nRemovendo o elemento 6 (raiz):")
arvore.remover(6)

print("Árvore após remoção (em ordem):")
arvore.em_ordem()