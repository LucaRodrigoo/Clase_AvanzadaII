import os
os.system('cls' if os.name == 'nt' else 'clear')

def compara_numeros (a,b,c):
    suma=a+b+c
    if suma> 15:
        resultado= max(a,b,c)
    elif suma<10:
        resultado = min(a,b,c)
    else:
        resultado =a+b+c-min(a,b,c)-max(a,b,c)
    return resultado

print (compara_numeros(8,2,3))

