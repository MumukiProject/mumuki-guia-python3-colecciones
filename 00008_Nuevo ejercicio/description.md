 Refactorizar código de forma tal que una lista no pueda tener elementos repetidos a la hora de agregarle nuevos. Deberían hacer un "agregar" nuevo con un if y un for. A raíz de esto contar que hay una estructura que ya nos soluciona ese problema. 
 
 class Biblioteca:
  def __init__(self):
    self.libros = []

  def agregar_libro(self, libro):
    if libro not in libros:
      self.libros.append(libro)

  def libros_largos(self):
    return [libro for libro in self.libros if libro.es_largo()]
  
  def  titulos_disponibles(self):
    return [libro.titulo for libro in self.libros]