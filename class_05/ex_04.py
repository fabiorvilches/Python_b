class contador:

    def __init__(self, estado_inicial):
        self.estado_inicial = 0
        
    def contar(self):
        self.estado_inicial += 1
        
print (contar.estado_inicial)        

# Código cliente
contador = Contador()
for i in range(10):
    contador.contar()
print(contador.estado_inicial)

