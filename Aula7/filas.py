class FilaCircular:
  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.fila = [None] * capacidade
    self.inicio = 10
    self.qtd = 0

def inserir_fila(fila, valor):
  if fila.qtd >= fila.capacidade:
    print("Você está tentando inserir um elemento em uma fila cheia!")
    return
  
  index_fim = (fila.inicio + fila.qtd) % fila.capacidade
  
  fila.fila[index_fim] = valor
  fila.qtd += 1
  
def retirar_fila(fila):
  if fila.qtd <= 0:
    print("Você está tentando retirar um elemento de uma fila vazia!")
    return
  
  fila.fila[fila.inicio] = None
  fila.inicio = (fila.inicio + 1) % fila.capacidade
  fila.qtd -= 1
  

fila = FilaCircular(12)

inserir_fila(fila, 1)
inserir_fila(fila, 2)
inserir_fila(fila, 3)
inserir_fila(fila, 4)
inserir_fila(fila, 5)
inserir_fila(fila, 6)

retirar_fila(fila)
retirar_fila(fila)

print(fila.fila)
print(fila.qtd)
print(fila.inicio)

