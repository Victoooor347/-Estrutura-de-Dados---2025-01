class Jogador:
    def __init__(self, info):
        self.info = info
        self.prox = None

def insert_jogador(jogador, info): # inserir jogador
    novo_jogador = Jogador(info)

    if jogador is None:
        novo_jogador.prox = novo_jogador
        return novo_jogador

    atual = jogador

    while atual.prox != jogador:
        atual = atual.prox

    atual.prox = novo_jogador
    novo_jogador.prox = jogador

    return jogador  

def roleta(jogador): # jogo
    if jogador is None:
        print("Não há jogadores!")
        return
    
    count = 1 # armazenar o num de jogadores
    atual = jogador
    while atual.prox != jogador: # contar quantos jogadores tem
        count += 1
        atual = atual.prox
    
    while count > 1: # rodar até sobrar 1 jogador
        eliminar = random.randint(1, count) # gerar num aleatório para eliminar jogador
        
        anterior = None
        atual = jogador
        
        for i in range(eliminar): # rodar até achar o jogador sorteado 
            anterior = atual
            atual = atual.prox   
        print(f"Jogador {atual.info} foi eliminado")
        anterior.prox = atual.prox
        jogador = atual.prox  
        count -= 1
    
    print(f"O jogador {jogador.info} venceu!")
    return jogador

import random # para conseguir gerar um num aleatório

jogador = None
for i in range(1, 10): # gerar quantidade x de jogadores
    jogador = insert_jogador(jogador, i) # inserir jogadores

roleta(jogador) # iniciar a roleta