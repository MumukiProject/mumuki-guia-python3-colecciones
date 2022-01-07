Modificar la lista del ejercicio 7 para que sea un set y el método que era un agregar sin repetidos para que prueben que sigue funcionando aún sin un if que verifique que el elemento no exista.

class Biblioteca:
  def __init__(self):
    self.libros = set()

  def agregar_libro(self, libro):
    self.libros.add(libro)

  def libros_largos(self):
    return [libro for libro in self.libros if libro.es_largo()]
  
  def  titulos_disponibles(self):
    return [libro.titulo for libro in self.libros]