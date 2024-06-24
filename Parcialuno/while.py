#imprimir 10 valores con while
i = 0
while i <= 10:
    print (i)
    i +=1

# print("ciclo controlado por banderin")
# while True:
#     entrada = input("ingresa S para salir:")
#     if entrada.upper == 's':
#         break
#     print("Escribiste: " + entrada)

# print("ciclo controlado por banderin 2")
# bandera ="x"
# while bandera != 'S':
#     bandera= input("ingresa S para salir:")

print("ciclo controlado por banderin 2")
bandera =True
while bandera != False :
    bandera= input("ingresa S para salir:")
    print(bandera.upper())
    salir=bandera.upper()
    if salir == 'S':
        bandera = False
        print("saliste del ciclo") 