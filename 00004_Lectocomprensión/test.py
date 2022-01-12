
  def setUp(self):
    self.un_libro_corto = Libro("Socorro", 299, "Terror")
    self.segundo_libro_corto = Libro("Fundación", 300, "Ciencia ficción")
    self.tercer_libro_corto = Libro("Historias de cronopios y de famas", 153, "Cuento y novela")
    self.un_libro_largo = Libro("Curtis Biología", 1164, "Ciencia")
    self.segundo_libro_largo = Libro("El nudo de la conciencia", 464, "Divulgación")
    self.tercer_libro_largo = Libro("La insoportable levedad del ser", 336, "Novela")
    self.cuarto_libro_largo = Libro("El hobbit", 310, "Novela")
    
  def test_Si_a_una_biblioteca_con_tres_libros_largos_le_enviamos_el_mensaje_libros_largos_nos_retorna_esos_tres_libros(self):
    biblioteca = Biblioteca()
    biblioteca.libros = [self.un_libro_largo, self.segundo_libro_largo, self.tercer_libro_largo, self.un_libro_corto]
    self.assertEqual(biblioteca.libros_largos(), [self.un_libro_largo, self.segundo_libro_largo, self.tercer_libro_largo])
    
  def test_Si_a_una_biblioteca_con_cuatro_libros_largos_le_enviamos_el_mensaje_libros_largos_nos_retorna_esos_cuatro_libros(self):
    biblioteca = Biblioteca()
    biblioteca.libros = [self.un_libro_largo, self.segundo_libro_largo, self.tercer_libro_largo, self.un_libro_corto, self.cuarto_libro_largo]
    self.assertEqual(biblioteca.libros_largos(), [self.un_libro_largo, self.segundo_libro_largo, self.tercer_libro_largo, self.cuarto_libro_largo])
    
  def test_Si_a_una_biblioteca_con_ningún_libro_largos_le_enviamos_el_mensaje_libros_largos_nos_retorna_una_lista_vacía(self):
    un_libro_corto = Libro("Socorro", 299, "Terror")
    segundo_libro_corto = Libro("Fundación", 300, "Ciencia ficción")
    tercer_libro_corto = Libro("Historias de cronopios y de famas", 153, "Cuento y novela")
    biblioteca = Biblioteca()
    biblioteca.libros = [self.un_libro_corto, self.segundo_libro_corto, self.tercer_libro_corto]
    self.assertEqual(biblioteca.libros_largos(), [])