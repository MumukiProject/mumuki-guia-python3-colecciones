Hacer un método que filtre sobre esa lista de instancias con listas por comprensión.

# Ejercicio 4

class Biblioteca:
  def __init__(self):
    self.libros = []

  def agregar_libro(self, libro):
    self.libros.append(libro)

  def libros_largos(self):
    return [libro for libro in self.libros if libro.es_largo()]
