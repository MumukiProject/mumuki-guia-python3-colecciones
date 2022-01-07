Mostrar un diccionario de instancias (o no) pero que sea atributo y lo mismo que con las listas en cuestiones de sintaxis de método vs proc/func.

# Ejercicio 6

class Libro:
  def __init__(self, titulo, cant_paginas, genero, artista):
    self.titulo = titulo
    self.cantidad_paginas = cant_paginas
    self.genero = genero
    self.artista = artista

  def es_largo(self):
    return self.cantidad_paginas > 350
  
  def nacionalidad(self):
    return self.artista["nacionalidad"]
