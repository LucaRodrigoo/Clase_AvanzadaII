import os
os.system('cls' if os.name == 'nt' else 'clear')

mi_diccionario = {"curso":"Python TOTAL","clase":"Diccionarios"}
print(mi_diccionario)

mi_diccionario["recursos"] = ["notas","ejercicios","examenes","proyectos"]

print(mi_diccionario)

print(mi_diccionario["recursos"][3])
