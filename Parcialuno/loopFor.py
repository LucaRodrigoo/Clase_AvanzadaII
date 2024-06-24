import os
os.system('cls' if os.name == 'nt' else 'clear')

# #ciclo for
# for i in range(10):
#     print(i)

# for i in range(1,20,2):
#     print(i)

# #ciclo for con listas
# lista= ["uno","dos","tres","cuatro","cinco"]
# for item in lista:
#     print(item)

# #invertir el orden de una lista
# for item in reversed(lista):
#     print(item)

# #ciclo for con tuplas
# tupla= ("uno","dos","tres","cuatro","cinco")
# for item in tupla:
#     print(item)

# #ciclo for con diccionarios
# diccionario = {
#     "curso": "Python Total", 
#     "clase": "Ciclos",
#     "tema": "For",
#     "Duracion": "1 Trimestre",
#     "profesor": "Luis Teruel"
# }
# print (diccionario)
# for llave in diccionario:
#     print(llave, ":", diccionario[llave])

numero= int (input("Ingresa un numero: "))
for i in range(1,11):
    print (i, "x", numero, "=", i*numero)