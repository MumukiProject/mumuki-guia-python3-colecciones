class Libro:
  def __init__(self, un_titulo, cant_paginas, un_genero):
    self.titulo = un_titulo
    self.paginas = cant_paginas
    self.genero = un_genero
    
  def es_largo(self):
    return self.paginas > 300

un_libro_corto = Libro("Socorro", 299, "Terror")
segundo_libro_corto = Libro("Fundación", 300, "Ciencia ficción")
tercer_libro_corto = Libro("Historias de cronopios y de famas", 153, "Cuento y novela")
un_libro_largo = Libro("Curtis Biología", 1164, "Ciencia")
segundo_libro_largo = Libro("El nudo de la conciencia", 464, "Divulgación")
tercer_libro_largo = Libro("La insoportable levedad del ser", 336, "Novela")
cuarto_libro_largo = Libro("El hobbit", 310, "Novela")