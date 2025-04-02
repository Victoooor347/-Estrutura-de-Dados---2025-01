

# CÓDIGO DO CHAT, NÃO CONSEGUI TENTAR FAZER MAS COLOQUEI NO CHAT PARA VER MAIS OU MENOS COMO É A ESTRUTURA DE TODO O CÓDIGO EM SI





import random

class Lista:
    def __init__(self, info):
        self.info = info  # info será um dicionário {id: X, hp: Y}
        self.prox = None

def criar_cavaleiro(id):
    hp = random.randint(50, 100)
    return {'id': id, 'hp': hp}

def inserir_cavaleiro(lista, id):
    novo_cavaleiro = Lista(criar_cavaleiro(id))
    
    if lista is None:
        novo_cavaleiro.prox = novo_cavaleiro
        return novo_cavaleiro
    
    atual = lista
    while atual.prox != lista:
        atual = atual.prox
    
    atual.prox = novo_cavaleiro
    novo_cavaleiro.prox = lista
    
    return lista

def mostrar_cavaleiros(lista):
    if lista is None:
        print("Arena vazia!")
        return
    
    atual = lista
    while True:
        cav = atual.info
        print(f"Cavaleiro {cav['id']} (HP: {cav['hp']})")
        atual = atual.prox
        if atual == lista:
            break
    print()

def ataque_cavaleiro(atacante):
    dano = random.randint(5, 10)
    print(f"Cavaleiro {atacante.info['id']} ataca causando {dano} de dano!")
    return dano

def simular_batalha(lista, num_cavaleiros):
    # Inicializa a arena com cavaleiros
    for i in range(1, num_cavaleiros + 1):
        lista = inserir_cavaleiro(lista, i)
    
    print("=== INÍCIO DA BATALHA ===")
    mostrar_cavaleiros(lista)
    
    atual = lista
    while True:
        # Verifica se há apenas um cavaleiro
        if atual.prox == atual:
            campeao = atual.info
            print(f"\n=== FIM DA BATALHA ===")
            print(f"Cavaleiro {campeao['id']} é o CAMPEÃO com {campeao['hp']} HP!")
            break
        
        # O cavaleiro atual ataca o próximo
        proximo = atual.prox
        dano = ataque_cavaleiro(atual)
        proximo.info['hp'] -= dano
        
        print(f"Cavaleiro {proximo.info['id']} sofreu {dano} de dano (HP restante: {proximo.info['hp']})")
        
        # Verifica se o cavaleiro foi derrotado
        if proximo.info['hp'] <= 0:
            print(f"Cavaleiro {proximo.info['id']} foi ELIMINADO!")
            
            # Remove o cavaleiro derrotado
            if proximo == lista:
                # Caso especial: removendo o primeiro elemento
                ultimo = lista
                while ultimo.prox != lista:
                    ultimo = ultimo.prox
                ultimo.prox = lista.prox
                lista = lista.prox
            else:
                # Remove um elemento do meio
                anterior = atual
                while anterior.prox != proximo:
                    anterior = anterior.prox
                anterior.prox = proximo.prox
            
            # Mostra situação atual
            mostrar_cavaleiros(lista)
        
        # Próximo cavaleiro atacante
        atual = atual.prox

# Programa principal
if __name__ == "__main__":
    lista = None
    num_cavaleiros = int(input("Quantos cavaleiros entrarão na arena? "))
    simular_batalha(lista, num_cavaleiros)