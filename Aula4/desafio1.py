
class Jogo:
    def __init__(self, info):
        self.info = info
        self.prox = None

def insert_jogador(jogador, info): 
    novo_jogador = Jogo(info)

    if jogador is None:
        novo_jogador.prox = novo_jogador
        return novo_jogador

    atual = jogador

    while atual.prox != jogador:
        atual = atual.prox

    atual.prox = novo_jogador
    novo_jogador.prox = jogador

    return jogador  

def batata_quente(jogador): 
    if jogador is None:
        print("Não há jogadores!")
        return
    
    count = 1 
    atual = jogador
    while atual.prox != jogador: 
        count += 1
        atual = atual.prox
    
    while count > 1:
        eliminar = random.randint(1, count) 
        
        anterior = None
        atual = jogador
        
        for i in range(eliminar): 
            anterior = atual
            atual = atual.prox   
        print(f"Jogador {atual.info} foi eliminado")
        anterior.prox = atual.prox
        jogador = atual.prox  
        count -= 1
    
    print(f"O jogador {jogador.info} venceu!")
    return jogador

import random 

jogador = None
for i in range(1, 10): 
    jogador = insert_jogador(jogador, i)

batata_quente(jogador) 