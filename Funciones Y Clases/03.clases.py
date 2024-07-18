class persona:
    #atributo de clase
    especie = "humano"

    #metodo de instancia
    def saludar(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print (f'hola, mi nombre es {self.nombre}')

    def cumplir_anios(self, estado_humor):
        print(f'cumplir {self.anios +1} años me pone  {estado_humor}')


