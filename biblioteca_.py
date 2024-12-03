class Libro:
     
    def __init__(self, titulo, autor, año, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = disponible

    def mostrar_informacion(self):
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.año}, Disponibilidad: {disponibilidad}"

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' ha sido prestado."
        else:
            return f"El libro '{self.titulo}' no esta disponible."

    def devolver(self):
        self.disponible = True
        return f"El libro '{self.titulo}' ha sido devuelto."
    
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        return f"El libro '{libro.titulo}' ha sido añadido a la biblioteca"

    def mostrar_libros(self):
        for libro in self.libros:
               print(libro.mostrar_informacion())
               if libro in self.libros == libro.prestar():
                    self.disponible = False
               elif not libro in self.libros == libro.prestar():
                    self.disponible = True
            
        
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro.mostrar_informacion() 
        else:
            return f"'{titulo}' no se encuentra en esta biblioteca"
                
                
    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if libro == titulo:
            libro.prestar()
            return f"El libro '{self.titulo}' ha sido prestado."
             
        else:
            return f"El libro '{titulo}' no se encuentra en la biblioteca."
        
#Añadir libros (seguir el ejemplo)
libro1 = Libro("El Quijote", "Miguel de Cervantes", 1605)
#libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
#libro3 = Libro("La llamada de lo Salvaje", "El Faliyo", 1999) 

#Añadir libros siguiendo el ejemplo
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
#biblioteca.agregar_libro(libro2)
#biblioteca.agregar_libro(libro3)

#Mostrar mensaje "el libro ha sido añadido" (seguir el ejemplo)
print(biblioteca.agregar_libro(libro1))
#print(biblioteca.agregar_libro(libro2))
#print(biblioteca.agregar_libro(libro3)) 


#Prestar un libro (seguir el ejemplo) 
# Al ejecutar mostrar_libros() despues de prestar() deberia aparecer dicho libro con
#el atributo "disponibilidad" como "No disponible"
print(libro1.prestar())
#print(biblioteca.mostrar_libros()) #(opcional)

#Devolver un libro (seguir el ejemplo)
# Al ejecutar devolver() despues de prestar() deberia aparecer dicho libro con
#el atributo "disponibilidad" como "Disponible"
print(libro1.devolver())
#print(biblioteca.mostrar_libros()) #(opcional)


#Buscar libro por nombre y mostrar en consola la info del libro (seguir el ejemplo)
print(biblioteca.buscar_libro("El Quijote"))
#print(biblioteca.buscar_libro("Cien Años de Soledad"))
#print(biblioteca.buscar_libro("La llamada de lo Salvaje"))
#print(biblioteca.mostrar_libros())



