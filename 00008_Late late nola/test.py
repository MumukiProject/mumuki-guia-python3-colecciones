	
  def test_si_una_biblioteca_recibe_el_mensaje_agregar_libro_se_agrega_un_libro_a_sus_libros_si_no_lo_tiene(self):
    biblioteca = Biblioteca()
    biblioteca.agregar_libro("Fundación")
    self.assertEqual(biblioteca.libros, ["Fundación"])

  def test_si_una_biblioteca_recibe_el_mensaje_agregar_libro_dos_veces_se_agregan_dos_libros_a_sus_libros_si_no_los_tiene(self):
    biblioteca = Biblioteca()
    biblioteca.agregar_libro("Socorro")
    biblioteca.agregar_libro("El lobo estepario")
    self.assertEqual(biblioteca.libros, ["Socorro", "El lobo estepario"])

  def test_si_una_biblioteca_recibe_el_mensaje_agregar_libro_no_hace_nada_si_ya_tiene_el_libro(self):
    biblioteca = Biblioteca()
    biblioteca.agregar_libro("Fundación")
    self.assertEqual(biblioteca.libros, ["Fundación"])

    
  