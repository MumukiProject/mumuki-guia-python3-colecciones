  
  def setUp(self):
    self.un_libro_corto = Libro("Socorro", 299, "Terror")
    self.segundo_libro_corto = Libro("Fundación", 300, "Ciencia ficción")
    self.tercer_libro_corto = Libro("Historias de cronopios y de famas", 153, "Cuento y novela")
    self.un_libro_largo = Libro("Curtis Biología", 1164, "Ciencia")
    self.segundo_libro_largo = Libro("El nudo de la conciencia", 464, "Divulgación")
    self.tercer_libro_largo = Libro("La insoportable levedad del ser", 336, "Novela")
    self.cuarto_libro_largo = Libro("El hobbit", 310, "Novela")
    
  def test_Si_a_una_biblioteca_con_cinco_libros_le_enviamos_el_mensaje_titulos_disponibles_obtenemos_el_titulo_de_esos_libros(self):
    biblioteca = Biblioteca()
    biblioteca.libros = [self.un_libro_largo, self.segundo_libro_largo, self.tercer_libro_largo, self.un_libro_corto, self.cuarto_libro_largo]
    self.assertEqual(biblioteca.titulos_disponibles(), ["Curtis Biología", "El nudo de la conciencia", "La insoportable levedad del ser", "Socorro", "El hobbit"])

  def test_Si_a_una_biblioteca_con_dos_libros_le_enviamos_el_mensaje_titulos_disponibles_obtenemos_el_titulo_de_esos_libros(self):
    biblioteca = Biblioteca()
    biblioteca.libros = [self.un_libro_corto, self.segundo_libro_corto]
    self.assertEqual(biblioteca.titulos_disponibles(), ["Socorro", "Fundación"])
    
  def test_Si_a_una_biblioteca_vacía_le_enviamos_el_mensaje_titulos_disponibles_obtenemos_una_lista_vacía(self):
    biblioteca = Biblioteca()
    self.assertEqual(biblioteca.titulos_disponibles(), [])
