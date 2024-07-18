#clase de operaciones aritmeticas
class OperacionesAritmeticas:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    #suma
    def suma(self):
        print(self.a +self.b)
    
    def potencia(self,a,b):
        print(a**b)

op= OperacionesAritmeticas(int(input("Ingrese a:")),int(input("Ingrese b:")))
op.suma()
op.potencia(5,5)