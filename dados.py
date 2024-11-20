class Dados:
    
    def __init__(self, tamanho):
        
        # inicializa uma lista com base no argumento tamanho com zeros em todas as entradas
        self.lista = [0] * tamanho
        self.tamanho = tamanho
        
        
    # Administra o tamanho da lista para garantir que não passe de self.tamanho elementos
    def add(self, valor):
        # Remove o primeiro elemento da lista
        self.lista.pop(0)
            
        # Adiciona um elemento na última posição da lista
        self.lista.append(valor)

  
    # Faz um print da lista na tela
    def mostrar(self):
        print(self.lista)
        
    
    def getAverage(self):
        return sum(self.lista) / len(self.lista)
