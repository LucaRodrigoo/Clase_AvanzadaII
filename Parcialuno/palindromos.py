import os
os.system('cls' if os.name == 'nt' else 'clear')

print("Ingrese una palabra:").upper()
palabra=input()

palindromo= palabra[::-1]

if (palindromo == palabra):
    print("La palabra es un palindromo")
else:
    print("No es un palindromo.")
