import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Ingrese una palabra:".lower())
palabra=input()

print("ingrese 3 letras a buscar: ")
letra1=input().lower()
letra2=input().lower()
letra3=input().lower()

print("La palabra tiene",palabra.count(letra1))
print("La palabra tiene",palabra.count(letra2))
print("La palabra tiene",palabra.count(letra3))

