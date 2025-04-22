
class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * 12
        self.inicio = 0
        self.qtd = 0

def insert(fila, value):
    if fila.qtd >= fila.capacidade:
        print("fila cheia")
        return
    
    index_fim = (fila.inicio + fila.qtd) % 12
    fila.fila[index_fim] = value
    fila.qtd += 1

def remove(fila, value):
    if fila.qtd <= 0:
        print("fila vazia")
        return
    
    print(f"{fila.fila[fila.inicio]} foi removido(a)")
    fila.fila[fila.inicio] = None
    fila.inicio = (fila.inicio + 1) % fila.capacidade
    fila.qtd -= 1


fila = FilaCircular(12)

insert(fila, "victor")
insert(fila, "gaby")
insert(fila, "isa")
insert(fila, "emilly")
insert(fila, "fabio")
print(fila.fila)

print("===============================")

remove(fila, "victor")
print(fila.fila)
print(f"ainda restam {fila.qtd} pessoas serem atendidas")
print(f"o próximo a ser atendido é {fila.fila[fila.inicio]}")