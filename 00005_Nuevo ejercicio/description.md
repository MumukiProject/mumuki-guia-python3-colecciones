Hacer un método que mappeé sobre esa lista de instancias con listas por comprensión.

class Biblioteca:
  def __init__(self):
    self.libros = []

  def agregar_libro(self, libro):
    self.libros.append(libro)

  def libros_largos(self):
    return [libro for libro in self.libros if libro.es_largo()]
  
  def  titulos_disponibles(self):
    return [libro.titulo for libro in self.libros]