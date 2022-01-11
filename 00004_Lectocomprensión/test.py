
  def setUp(self):
    un_libro_corto = Libro("Socorro", 299, "Terror")
    segundo_libro_corto = Libro("Fundación", 300, "Ciencia ficción")
    tercer_libro_corto = Libro("Historias de cronopios y de famas", 153, "Cuento y novela")
    un_libro_largo = Libro("Curtis Biología", 1164, "Ciencia")
    segundo_libro_largo = Libro("El nudo de la conciencia", 464, "Divulgación")
    tercer_libro_largo = Libro("La insoportable levedad del ser", 336, "Novela")
    cuarto_libro_largo = Libro("El hobbit", 310, "Novela")
    
  def test_Si_a_una_biblioteca_con_tres_libros_largos_le_enviamos_el_mensaje_libros_largos_nos_retorna_esos_tres_libros(self):
    self.setUp():
    biblioteca = Biblioteca()
    biblioteca.libros = [un_libro_largo, segundo_libro_largo, tercer_libro_largo, un_libro_corto]
    self.assertEqual(biblioteca.libros_largos(), [un_libro_largo, segundo_libro_largo, tercer_libro_largo])
