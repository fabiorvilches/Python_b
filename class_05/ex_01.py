class Usuario:
    
    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade

usuario = Usuario(id=1, nome='Fabio', idade=49)
usuario2 = Usuario(id=2, nome='Cory', idade=0)

print (usuario.id)
print (usuario.nome)
print (usuario.idade)

