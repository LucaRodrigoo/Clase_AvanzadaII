class Personaje:
    def __init__(self,nombre,arma):
        self.nombre=nombre
        self.arma=arma

class Mago(Personaje):
    pass

hechizero= Mago("Merlin","Caldero")
print(hechizero.nombre)
print(hechizero.arma)
