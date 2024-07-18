#utilizar la clase 00ClasesEspeciales
import os
os.system('cls' if os.name == 'nt' else 'clear')

#importar class libro
from ClasesEspeciales import Libro

libro1= Libro ("Stephen King","It", 1032)
print(libro1)