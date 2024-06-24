#Division

dividendo= input(("Escriba el primer numero: "))
divisor= input(("Escriba el segundo numero: "))

division= (dividendo / divisor)
if divisor == 0:
    print ("Error, No puede ser el divisor 0.")
elif divisor != 0:
    print ("La respuesta es: ", division)
