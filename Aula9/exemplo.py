class No:
  def __init__(self, chave):
    self.chave = chave
    self.direita = None
    self.esquerda = None
    
  def __repr__(self):
    return '%s <- %s -> %s' % (
      self.esquerda and self.esquerda.chave,
      self.chave,
      self.direita and self.direita.chave
    )

def insert(no, chave):
  if no is None:
    return No(chave)
  if chave < no.chave:
    no.esquerda = insert(no.esquerda, chave)
  else:
    no.direita = insert(no.direita, chave)
  
  return no

raiz = insert(None, 5)
raiz = insert(raiz, 2)
raiz = insert(raiz, 7)
raiz = insert(raiz, 6)
raiz = insert(raiz, 8)

print(raiz)
