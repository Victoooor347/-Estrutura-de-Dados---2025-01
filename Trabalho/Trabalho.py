
class ListaNode:            # estrutura de um nó da pilha
    def __init__(self, info):
        self.info = info
        self.prox = None

class Pilha:            # estrutura da pilha
    def __init__(self, capacidade, topo=None):
        self.topo = topo
        self.capacidade = capacidade
        self.num_elementos = 0

def pilha_push(pilha, valor):               
    if pilha.num_elementos >= pilha.capacidade:  # verifica se a pilha ta cheia
        print("Capacidade máxima alcançada!")
        return

    elemento = ListaNode(valor)
    elemento.prox = pilha.topo
    pilha.topo = elemento
    pilha.num_elementos += 1
    return pilha

def pilha_show(pilha):      # mostra o valor do topo da pilha
    atual = pilha.topo
    while atual != None:
        print(atual.info)
        atual = atual.prox

def pilha_pop(pilha):          # remove o topo da pilha
    if pilha.topo == None:
        print("Pilha vazia!")
    else:
        pilha.topo = pilha.topo.prox
        pilha.num_elementos -= 1

def pilha_vazia(pilha):     # verifica se a pilha ta vazia
    return pilha.topo == None

def pilha_pop_valor(pilha):  # mostra todos os valores da pilha
    if pilha.topo is None:
        raise Exception("Pilha vazia!")
    valor = pilha.topo.info
    pilha_pop(pilha)
    return valor

def precedencia(op):    # Define prioridade dos operadores
    if op == 'not':
        return 3
    elif op == 'and':
        return 2
    elif op == 'or':
        return 1
    return 0

def aplicar_operador(op, pilha_operandos):   # pega valores da pilha de operandos e aplica o operador que foi retirado da pilha de operadores
    if op == 'not':                             #retira um operando, aplica not e empilha o resultado
        if pilha_operandos.num_elementos < 1:
            print("Não tem operandos para 'not'") # mensagem de erro
        a = pilha_pop_valor(pilha_operandos)
        pilha_push(pilha_operandos, not a)
    elif op in ('and', 'or'):               # retira dois operandos, aplica um operador lógico e empilha o resultado
        if pilha_operandos.num_elementos < 2:
            print(f"Operandos insuficientes para '{op}'")
        b = pilha_pop_valor(pilha_operandos)
        a = pilha_pop_valor(pilha_operandos)
        if op == 'and':
            pilha_push(pilha_operandos, a and b)
        else:
            pilha_push(pilha_operandos, a or b)

def avaliar_expressao(expr):                                            # função principal
    tokens = expr.replace('(', ' ( ').replace(')', ' ) ').split()       # replace vai adicionar espaços antes e depois de cada () e split vai separar expressão por expressão
    pilha_operandos = Pilha(capacidade=len(tokens))                     # pilha true e false
    pilha_operadores = Pilha(capacidade=len(tokens))                    # pilha not,and,or,(,)

    for token in tokens:
        if token in ('True', 'False'):
            pilha_push(pilha_operandos, token == 'True')  # converte para string e empilha

        elif token in ('and', 'or', 'not'):                 # Enquanto tiver operadores com maior ou igual precedência, aplica eles primeiro e depois empilha o operador atual
            while (not pilha_vazia(pilha_operadores) and
                   pilha_operadores.topo.info != '(' and
                   precedencia(pilha_operadores.topo.info) >= precedencia(token)):
                op = pilha_pop_valor(pilha_operadores)
                aplicar_operador(op, pilha_operandos)
            pilha_push(pilha_operadores, token)

        elif token == '(':                  # só empilha (
            pilha_push(pilha_operadores, token)

        elif token == ')':                  # Quando encontra ), aplica todos os operadores até achar ( e remove o ele
            while (not pilha_vazia(pilha_operadores) and pilha_operadores.topo.info != '('):
                op = pilha_pop_valor(pilha_operadores)
                aplicar_operador(op, pilha_operandos)
            if pilha_vazia(pilha_operadores):
                print("Parênteses desbalanceados!")
            pilha_pop(pilha_operadores)  # remove '('

        else:
            print(f"Token inválido: {token}")

    while not pilha_vazia(pilha_operadores):            # aplica operadores restantes na pilha até que ela fique vazia
        if pilha_operadores.topo.info == '(':
            print("Parênteses desbalanceados!")
        op = pilha_pop_valor(pilha_operadores)
        aplicar_operador(op, pilha_operandos)

    if pilha_operandos.num_elementos != 1:   # se sobrar algo na pilha, houve um erro
        print("Expressão malformada!")

    return pilha_pop_valor(pilha_operandos)

expressao1 = "True and False"               
expressao2 = "not False"                
expressao3 = "True or False and False"      
expressao4 = "( True or False ) and False"  

print("Primeira Expressão: ", expressao1)
print("Resultado: ", avaliar_expressao(expressao1))
print("===========================================================")
print("Segunda Expressão: ", expressao2)
print("Resultado: ", avaliar_expressao(expressao2))
print("===========================================================")
print("Terceira Expressão: ", expressao3)
print("Resultado: ", avaliar_expressao(expressao3))
print("===========================================================")
print("Quarta Expressão: ", expressao4)
print("Resultado: ", avaliar_expressao(expressao4))