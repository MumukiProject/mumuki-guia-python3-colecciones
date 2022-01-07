Mostrar que se pueden tener listas de instancias. Puede ser un atributo o algo más. A definir (probablemente un atributo, después vemos si seguimos con el mismo dominio o con otro).

# Ejercicio 3
# Esto lo hacemos para mostrar que no hay que 
# cambiar nada en la clase Biblioteca porque se pueden tener colecciones de instancias.

class Libro:
  def __init__(self, titulo, cant_paginas, genero):
    self.titulo = titulo
    self.cantidad_paginas = cant_paginas
    self.genero = genero

  def es_largo(self):
    return self.cantidad_paginas > 350
