import time
import random

colores = ['amarillo', 'azul', 'verde', 'rojo']
usuarios = [{'Nombre':'Josep'}, {'Nombre':'Claudio'}, {'Nombre':'Isabel'}, {'Nombre':'Sheila'}]

#Añadimos un nuevo color
def añadir_color(colores):
    while True:
        color= input("Añade un color: ")
        while color == "":
            print("Porfavor, añade un color.")
            color = input("Añade un color: ")

        if color not in colores:
            colores.append(color.lower())
            print(f"Añadiendo color {color}...")
            break
        else:
            print(f"El color {color} ya está en la lista.")
    colores.sort()
    time.sleep(1)
    for color in colores:
        print(f"{color}", end =" | ")
    print() 

    if len(colores) > len(usuarios):
        time.sleep(1)
        print("Hay más colores que usuarios. Por favor, añade otro usuario.")
        time.sleep(2)
    añadir_usuario(usuarios, colores)    

#------------------------------------------------------------------------

#Añadimos usuario / Mostrar lista resultante
def añadir_usuario(usuarios, colores):
    usuario = input("\nAñade un nuevo usuario: ")
    while usuario == "":
        print("Este campo no puede quedar vacío.")
        time.sleep(1)
        usuario = input("Añade un nuevo usuario: ")
    usuarios.append({"Nombre": usuario.capitalize()})
    time.sleep(1)
    print(f"Genial! Acabas de añadir a {usuario.capitalize()}.")
    print("--------------------------")
    time.sleep(1)
    print("Actualizando datos...")
    time.sleep(1)
    for color in colores: 
        print(f"{color}", end=" | ") 
    time.sleep(1)
    print()
    for usuario in usuarios:
        print(f"{usuario['Nombre']}", end=" | ")   
    time.sleep(2)
    while len(usuarios) > len(colores):
        time.sleep(2)
        print("\nOops! Hay más usuarios que colores!")
        time.sleep(1)
        color = input("Añade un color: ")
        while color == "":
            print("Este campo no puede quedar vacio.")
            color = input("Añade un color: ")
        if color not in colores:
            colores.append(color.lower())
            time.sleep(1)
            print(f"Gracias! Acabas de añadir el color {color}.")
            time.sleep(1)
            for color in colores: 
                print(f"{color}", end=" | ")
            print()
            time.sleep(1)
            for usuario in usuarios: 
                print(f"{usuario['Nombre']}", end=" | ") 
    print()
    time.sleep(2)

#------------------------------------------------------------------------

#Asignamos colores a los usuarios aleatoriamente y nos aseguramos que no se repitan los colores eliminandolos de la lista una vez ocupados.
def asignar_colores(usuarios, colores):
    colores_disponibles = colores.copy()
    asignaciones = []
    time.sleep(2)
    print("Asignando colores aleatoriamente...")
    for usuario in usuarios:
        if colores_disponibles:
            color = random.choice(colores_disponibles)
            asignaciones.append((usuario, color))
            colores_disponibles.remove(color)
    time.sleep(3)   
    for usuario, color in asignaciones:
        print(f"{usuario['Nombre']}: {color}")
    print("--------------------------")
    time.sleep(2)

#------------------------------------------------------------------------

#Generar indice #:usuario
def mostrar_usuarios(usuarios):
    print("Generando índice...")
    time.sleep(2)
    for i, usuario in enumerate(usuarios):
        print(f"{i}: {usuario['Nombre']} ")
        time.sleep(1)
    print("Utiliza los índices para eliminar usuarios.")
    time.sleep(2)

#------------------------------------------------------------------------

#Eliminacion de usuario
def eliminar_usuarios(usuarios):
    while True:
        print()
        try:           
            time.sleep(1)
            borrado = int(input("Selecciona usuario a eliminar (ver índice: 0-4): "))
            if 0 <= borrado < len(usuarios):
                usuario_borrado = usuarios.pop(borrado)
                print(f"El usuario {usuario_borrado['Nombre']} ha sido eliminado.")
                print("--------------------------")
                time.sleep(2)
                break
            else:
                print("Índice fuera de rango.")
                time.sleep(1)
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")
            time.sleep(1)

#------------------------------------------------------------------------

#Mostrar lista ordenada 
def lista_final(usuarios):
    usuarios = sorted(usuarios, key=lambda x: x['Nombre'])
    print("Actualizando usuarios...")
    time.sleep(2)
    print("Ordenando alfabéticamente...")
    time.sleep(2)
    for usuario in usuarios:
        print(usuario['Nombre'])
    time.sleep(2)

#------------------------------------------------------------------------

#Diccionario funciones Interfaz Menu
acciones = { 
    '1': lambda: añadir_color(colores), 
    '2': lambda: añadir_usuario(usuarios, colores), 
    '3': lambda: asignar_colores(usuarios, colores), 
    '4': lambda: mostrar_usuarios(usuarios), 
    '5': lambda: eliminar_usuarios(usuarios), 
    '6': lambda: lista_final(usuarios) 
    }

#------------------------------------------------------------------------

#Interfaz Menu 
def programa_principal(): 
    while True: 
        print("\n<<----------MENU---------->>") 
        print("1. Añadir color") 
        print("2. Añadir usuario") 
        print("3. Asignar colores aleatoriamente") 
        print("4. Generar índice usuarios") 
        print("5. Eliminar usuario") 
        print("6. Lista final") 
        print("7. Salir")
        print("----------------------------")
        opcion = input("Selecciona una opción (1-7): ")
        if opcion == '7': 
            print("Hemos terminado!\nHasta pronto!") 
            break 
        elif opcion in acciones:
            acciones[opcion]() 
        else: 
            print("Opción no válida. Inténtalo de nuevo.")
            time.sleep(2)

#------------------------------------------------------------------------

#Llamada a ejecucion del programa
programa_principal()
