
  def setUp(self):
    self.socorro = Libro("Socorro", 299, "Terror", {"nombre": "Elsa", "apellido": "Bornemann", "nacionalidad": "Argentina" })

    self.como_agua = Libro("Como agua para chocolate", 216, "Realismo mágico", {"nombre": "Laura", "apellido": "Esquivel", "nacionalidad": "México" })

    self.cronopios = Libro("Historias de cronopios y de famas", 153, "Cuento y novela", {"nombre": "Julio", "apellido": "Cortázar", "nacionalidad": "Bélgica" })

    self.levedad = Libro("La insoportable levedad del ser", 336, "Novela", {"nombre": "Milan", "apellido": "Kundera", "nacionalidad": "Bélgica" })

  def test_los_libros_de_una_biblioteca_inicialmente_son_un_set_vacio(self):
    biblioteca = Biblioteca()
    self.assertEqual(biblioteca.libros, set())
    
  def test_si_una_biblioteca_recibe_el_mensaje_agregar_libro_se_agrega_un_libro_a_sus_libros_si_no_lo_tiene(self):
    biblioteca = Biblioteca()
    biblioteca.agregar_libro(self.levedad)
    self.assertEqual(biblioteca.libros, [self.levedad])

  def test_si_una_biblioteca_recibe_el_mensaje_agregar_libro_dos_veces_se_agregan_dos_libros_a_sus_libros_si_no_los_tiene(self):
    biblioteca = Biblioteca()
    biblioteca.agregar_libro(self.socorro)
    biblioteca.agregar_libro(self.como_agua)
    self.assertEqual(biblioteca.libros, [self.socorro, self.como_agua])

  def test_si_una_biblioteca_recibe_el_mensaje_agregar_libro_no_hace_nada_si_ya_tiene_el_libro(self):
    biblioteca = Biblioteca()
    biblioteca.agregar_libro(self.cronopios)
    biblioteca.agregar_libro(self.como_agua)
    self.assertEqual(biblioteca.libros, [self.cronopios, self.como_agua])
    biblioteca.agregar_libro(self.cronopios)
    self.assertEqual(biblioteca.libros, [self.cronopios, self.como_agua])