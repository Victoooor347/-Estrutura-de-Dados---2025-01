# Classe que implementa um Min Heap (Heap mínimo)
class MinHeap:
    def __init__(self):  # Construtor da classe
        self.heap = []  # Lista que representa a estrutura do heap

    # Insere um valor no heap e ajusta a posição com a função _subir
    def inserir(self, valor):
        self.heap.append(valor)  # Adiciona o valor no final da lista
        self._subir(len(self.heap) - 1)  # Corrige a posição do novo valor

    # Remove o menor elemento (raiz) do heap
    def remover(self):
        if not self.heap:  # Verifica se o heap está vazio
            print("Heap vazio. Nada para remover.")
            return None
        if len(self.heap) == 1:  # Se tiver apenas um elemento, remove direto
            return self.heap.pop()
        raiz = self.heap[0]  # Menor elemento (raiz)
        self.heap[0] = self.heap.pop()  # Move o último elemento para a raiz
        self._descer(0)  # Ajusta a posição correta com a função _descer
        return raiz  # Retorna o valor removido

    # Retorna o menor valor sem removê-lo
    def consultar(self):
        if not self.heap:  # Verifica se está vazio
            print("Heap vazio.")
            return None
        return self.heap[0]  # Retorna a raiz (menor elemento)

    # Imprime o conteúdo atual do heap
    def imprimir(self):
        print("Heap atual:", self.heap)

    # Função auxiliar para ajustar a posição do novo valor (subindo)
    def _subir(self, index):
        pai = (index - 1) // 2  # Calcula o índice do pai
        # Enquanto não estiver na raiz e o valor atual for menor que o pai
        while index > 0 and self.heap[index] < self.heap[pai]:
            # Troca os valores
            self.heap[index], self.heap[pai] = self.heap[pai], self.heap[index]
            index = pai  # Atualiza o índice para continuar subindo
            pai = (index - 1) // 2

    # Função auxiliar para ajustar a posição após remoção (descendo)
    def _descer(self, index):
        tamanho = len(self.heap)
        menor = index  # Começa assumindo que o menor é o próprio índice
        esquerda = 2 * index + 1  # Filho da esquerda
        direita = 2 * index + 2  # Filho da direita

        # Verifica se o filho da esquerda é menor que o atual
        if esquerda < tamanho and self.heap[esquerda] < self.heap[menor]:
            menor = esquerda
        # Verifica se o filho da direita é ainda menor
        if direita < tamanho and self.heap[direita] < self.heap[menor]:
            menor = direita
        # Se o menor não for o atual, troca e continua o processo recursivamente
        if menor != index:
            self.heap[index], self.heap[menor] = self.heap[menor], self.heap[index]
            self._descer(menor)

# Bloco principal para testar o heap com menu interativo
if __name__ == "__main__":  # Garante que só será executado se for o arquivo principal
    heap = MinHeap()
    while True:
        print("\n1. Inserir\n2. Remover\n3. Consultar\n4. Imprimir\n5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = int(input("Digite o valor a inserir: "))
            heap.inserir(valor)  # Chama a função de inserção
        elif opcao == '2':
            removido = heap.remover()  # Remove o menor valor
            if removido is not None:
                print(f"Removido: {removido}")
        elif opcao == '3':
            topo = heap.consultar()  # Consulta o menor valor
            if topo is not None:
                print(f"Menor elemento: {topo}")
        elif opcao == '4':
            heap.imprimir()  # Imprime a lista do heap
        elif opcao == '5':
            break  # Sai do loop
        else:
            print("Opção inválida.")
