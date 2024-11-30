#Registro de estudiantes
estudiantes = {}

#Funcion Añadir nuevo estudiante
def añadir_estudiante(nombre, edad, asignaturas):
    estudiantes[nombre] = {"Edad": edad, "Asignaturas": asignaturas}

#Funcion Actualizar info de estudiante
def actualizar_estudiante(nombre, edad=None, asignaturas=None):
    if nombre in estudiantes:
        if edad is not None:
            estudiantes[nombre]["Edad"] = edad
        if asignaturas is not None:
            estudiantes[nombre]["Asignaturas"] = asignaturas
    else:
        print(f"El estudiante {nombre} no esta registrado.")

#Funcion Mostrar lista de estudiantes
def mostrar_estudiantes():
    for nombre, detalles in estudiantes.items():
        print(f"Nombre: {nombre} | Edad: {detalles['Edad']} | Asignaturas: {", ".join(detalles["Asignaturas"])}")

#Llamado a funcion Añadir estudiantes
# #Añade siempre los nuevos estudiantes en este apartado siguiendo el mismo ejemplo de Ana/Luis. 
# Puedes copiar y pegar el codigo y simplemente reemplazar los datos de interes (Todos los que van entre comillas " " + la edad)
añadir_estudiante("Ana", 20, ["Matemáticas", "Fisica"])
añadir_estudiante("Luis", 22, ["Quimica", "Biologia"])       

#Llamado a funcion Mostrar lista de estudiantes
print("Lista de estudiantes:") #Añade almohadilla en esta linea para mostrar en consola la lista antigua 
mostrar_estudiantes() #Añade almohadilla en esta linea para mostrar en consola la lista antigua 

#Llamado a funcion Actualizar info estudiante 
actualizar_estudiante("Ana", asignaturas=["Matematicas", "Fisica", "Quimica"])

#Llamado a funcion Mostrar la lista de estudiantes actualizada
print("\nLista de estudiantes actualizada: ")
mostrar_estudiantes() 