class Dados:
    
    def __init__(self, tamanho):
        
        # inicializa uma lista com base no argumento tamanho com zeros em todas as entradas
        self.lista = [{"luminosidade": 0, "uv": 0} for i in range(tamanho)]
        self.tamanho = tamanho
        
        
    # Administra o tamanho da lista para garantir que não passe de self.tamanho elementos
    def add(self, luminosidade, uv):
        # Remove o primeiro elemento da lista
        self.lista.pop(0)
            
        valor = {"luminosidade": luminosidade, "uv": uv}
            
        # Adiciona um elemento na última posição da lista
        self.lista.append(valor)
    
    # Faz um print da lista na tela
    def mostrar(self):
        print(self.lista)
        
    
    def getAverage(self):
        lista_luminosidade = [ sub['luminosidade'] for sub in self.lista ]
        media_luminosidade = sum(lista_luminosidade) / len(lista_luminosidade)
        
        lista_uv = [ sub['uv'] for sub in self.lista ]
        media_uv = sum(lista_uv) / len(lista_uv)
        
        return {"luminosidade": media_luminosidade, "uv": media_uv}
    
    
    def reset(self):
        self.lista = [{"luminosidade": 0, "uv": 0} for i in range(self.tamanho)]
    
