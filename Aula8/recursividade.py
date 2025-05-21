
# def somatorio(n):
#     if n == 0:
#         return 0
#     return n + somatorio(n - 1)

# print(somatorio(10))


# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1 
#     return fibo(n - 1) + fibo(n - 2)


# print(fibo(7))


# def show(self):
#     atual = self.head

#     if atual == None:
#         print("")
#         return

#     while atual is not None:
#         print(atual.info)
#         atual = atual.prox

    
class No:
  def __init__(self, info):
    self.info = info
    self.prox = None
    
class ListaEncadeada:
  def __init__(self):
    self.head = None
    
  def insert(self, info):
    elemento = No(info)
    
    if self.head == None:
      self.head = elemento
      return
      
    atual = self.head
    
    while atual.prox  != None:
      atual = atual.prox
      
    atual.prox = elemento
    
  def show(self):
    atual = self.head

    while atual.prox != None:
      print(atual.info)
      atual = atual.prox
  
  def show_recursive(self):
    atual = self.head

    if atual == None:
    
    
    
    
lista = ListaEncadeada()

lista.insert(5)

print(lista.head.info)
