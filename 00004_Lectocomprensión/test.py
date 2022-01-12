
  def test_Si_a_una_biblioteca_con_tres_libros_largos_le_enviamos_el_mensaje_libros_largos_nos_retorna_esos_tres_libros(self):
    un_libro_corto = Libro("Socorro", 299, "Terror")
    segundo_libro_corto = Libro("Fundación", 300, "Ciencia ficción")
    tercer_libro_corto = Libro("Historias de cronopios y de famas", 153, "Cuento y novela")
    un_libro_largo = Libro("Curtis Biología", 1164, "Ciencia")
    segundo_libro_largo = Libro("El nudo de la conciencia", 464, "Divulgación")
    tercer_libro_largo = Libro("La insoportable levedad del ser", 336, "Novela")
    cuarto_libro_largo = Libro("El hobbit", 310, "Novela")
    biblioteca = Biblioteca()
    biblioteca.libros = [un_libro_largo, segundo_libro_largo, tercer_libro_largo, un_libro_corto]
    self.assertEqual(biblioteca.libros_largos(), [un_libro_largo, segundo_libro_largo, tercer_libro_largo])
    
    
  def test_Si_a_una_biblioteca_con_cuatro_libros_largos_le_enviamos_el_mensaje_libros_largos_nos_retorna_esos_cuatro_libros(self):
    un_libro_corto = Libro("Socorro", 299, "Terror")
    segundo_libro_corto = Libro("Fundación", 300, "Ciencia ficción")
    tercer_libro_corto = Libro("Historias de cronopios y de famas", 153, "Cuento y novela")
    un_libro_largo = Libro("Curtis Biología", 1164, "Ciencia")
    segundo_libro_largo = Libro("El nudo de la conciencia", 464, "Divulgación")
    tercer_libro_largo = Libro("La insoportable levedad del ser", 336, "Novela")
    cuarto_libro_largo = Libro("El hobbit", 310, "Novela")
    biblioteca = Biblioteca()
    biblioteca.libros = [un_libro_largo, segundo_libro_largo, tercer_libro_largo, un_libro_corto, cuarto_libro_largo]
    self.assertEqual(biblioteca.libros_largos(), [un_libro_largo, segundo_libro_largo, tercer_libro_largo, cuarto_libro_largo])
    
    
  def test_Si_a_una_biblioteca_con_ningún_libro_largos_le_enviamos_el_mensaje_libros_largos_nos_retorna_una_lista_vacía(self):
    un_libro_corto = Libro("Socorro", 299, "Terror")
    segundo_libro_corto = Libro("Fundación", 300, "Ciencia ficción")
    tercer_libro_corto = Libro("Historias de cronopios y de famas", 153, "Cuento y novela")
    biblioteca = Biblioteca()
    biblioteca.libros = [un_libro_corto, segundo_libro_corto, tercer_libro_corto]
    self.assertEqual(biblioteca.libros_largos(), [])