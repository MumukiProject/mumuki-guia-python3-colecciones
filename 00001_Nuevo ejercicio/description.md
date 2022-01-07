1. Mostrar que las listas existen en el mundo de los objetos agregando un atributo a una clase que sea una lista. Hacer algún método que haga algo con esa lista. Por ejemplo: agregar (list.append(atributo, elemento).

# Ejercicio 1
# En este punto los libros son strings con el título del libro
class Biblioteca:
  def __init__(self):
    self.libros = []

  def agregar_libro(self, libro):
    list.append(self.libros, libro)