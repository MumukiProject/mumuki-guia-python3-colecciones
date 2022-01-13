
  def setUp(self):
    self.socorro = Libro("Socorro", 299, "Terror", {"nombre": "Elsa", "apellido": "Bornemann", "nacionalidad": "Argentina" })

    self.como_agua = Libro("Como agua para chocolate", 216, "Realismo mágico", {"nombre": "Laura", "apellido": "Esquivel", "nacionalidad": "México" })

    self.cronopios = Libro("Historias de cronopios y de famas", 153, "Cuento y novela", {"nombre": "Julio", "apellido": "Cortázar", "nacionalidad": "Bélgica" })

    self.levedad = Libro("La insoportable levedad del ser", 336, "Novela", {"nombre": "Milan", "apellido": "Kundera", "nacionalidad": "Bélgica" })

  def test_los_libros_de_una_biblioteca_inicialmente_son_un_set_vacio(self):
    biblioteca = Biblioteca()
    self.assertEqual(biblioteca.libros, set())
    
  def test_Si_a_una_biblioteca_con_tres_libros_largos_le_enviamos_el_mensaje_libros_largos_nos_retorna_esos_tres_libros(self):
    biblioteca = Biblioteca()
    biblioteca.libros = [self.un_libro_largo, self.segundo_libro_largo, self.tercer_libro_largo, self.un_libro_corto]
    self.assertEqual(biblioteca.libros_largos(), [self.un_libro_largo, self.segundo_libro_largo, self.tercer_libro_largo])
    
  def test_Si_a_una_biblioteca_con_cuatro_libros_largos_le_enviamos_el_mensaje_libros_largos_nos_retorna_esos_cuatro_libros(self):
    biblioteca = Biblioteca()
    biblioteca.libros = [self.un_libro_largo, self.segundo_libro_largo, self.tercer_libro_largo, self.un_libro_corto, self.cuarto_libro_largo]
    self.assertEqual(biblioteca.libros_largos(), [self.un_libro_largo, self.segundo_libro_largo, self.tercer_libro_largo, self.cuarto_libro_largo])
    
  def test_Si_a_una_biblioteca_con_ningún_libro_largos_le_enviamos_el_mensaje_libros_largos_nos_retorna_una_lista_vacía(self):
    biblioteca = Biblioteca()
    biblioteca.libros = [self.un_libro_corto, self.segundo_libro_corto, self.tercer_libro_corto]
    self.assertEqual(biblioteca.libros_largos(), [])