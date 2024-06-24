# Jose David Mejia Mendoza 31 años
# Kennet Andersson Martinez Varela 21 años
# Tomy José Montúfar Zuniga 19 años
# Ángel Antonio Pérez Rodríguez 18 años
# José Eduardo Sabillón Hurtado 19 años
# Diany Lizbeth Enamorado Fernández 19 años
# Anderson Jair Garcia Menjivar 19 años
# Iliana Liceth Zuniga Enamorado, 18 años
# Derick Dair Muñoz Iraheta, 20 años
# Norman Bú, 25 años.#
# Arnold Stanly Ford, 18 años
# Walter Eduardo Rapalo Smith, 20 años
# Edson Jhair Ríos coto, 26 años
# Jorge Arturo Vallecillo Espinoza 18 años
# Lucas Rodrigo Bautista Juarez 18 años

diccionario = {
    "Jose David Mejia Mendoza": (31, "contraseña1"),
    "Kennet Andersson Martinez Varela": (21, "contraseña2"),
    "Tomy José Montúfar Zuniga": (19, "contraseña3"),
    "Ángel Antonio Pérez Rodríguez": (18, "contraseña4"),
    "José Eduardo Sabillón Hurtado": (19, "contraseña5"),
    "Diany Lizbeth Enamorado Fernández": (19, "contraseña6"),
    "Anderson Jair Garcia Menjivar": (19, "contraseña7"),
    "Iliana Liceth Zuniga Enamorado": (18, "contraseña8"),
    "Derick Dair Muñoz Iraheta": (20, "contraseña9"),
    "Norman Bú": (25, "contraseña10"),
    "Arnold Stanly Ford": (18, "contraseña11"),
    "Walter Eduardo Rapalo Smith": (20, "contraseña12"),
    "Edson Jhair Ríos Coto": (26, "contraseña13"),
    "Jorge Arturo Vallecillo Espinoza": (18, "contraseña14"),
    "Lucas Rodrigo Bautista Juarez": (18, "contraseña15")
}

# Sistema de inicio de sesión
nombre_ingresado = input("Por favor, ingrese su nombre: ")
contraseña_ingresada = input("Por favor, ingrese su contraseña: ")

if nombre_ingresado in diccionario and contraseña_ingresada == diccionario[nombre_ingresado][1]:
    print("Inicio de sesión exitoso.")
        #Imprimir el diccionario
    nombre_ingresado2 = input("Por favor, ingrese un nombre: ")

    if nombre_ingresado2 in diccionario:
        print(diccionario[nombre_ingresado2])
    else:
        print("El nombre no existe en el diccionario.")

else:
    print("Nombre o contraseña incorrectos. Por favor, intente de nuevo.")


