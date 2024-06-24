#Operaciones aritmeticas

import os
os.system('cls' if os.name == 'nt' else 'clear')

a= int(input("Ingresa el primer numero: "))
y= int(input("Ingresa el segundo numero: "))

print ("Suma:",a+y)
print ("Resta:",a-y)
print ("Multiplicacion:",a*y)
print ("Division:",a/y)

if a== 0:
    print ("No se puede dividir entre 0")
else:
    x = -y/a
    print ("")