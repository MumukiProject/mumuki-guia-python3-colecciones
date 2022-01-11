
  def test_una_biblioteca_inicialmente_no_tiene_libros(self):
    biblioteca = Biblioteca()
    self.assertEqual(biblioteca.libros, [])

  def test_si_una_biblioteca_recibe_el_mensaje_agregar_libro_se_agrega_un_libro_a_sus_libros(self):
    biblioteca = Biblioteca()
    biblioteca.agregar_libro("Fundación")
    self.assertEqual(biblioteca.libros, ["Fundación"])

  def test_si_una_biblioteca_recibe_el_mensaje_agregar_libro_dos_veces_se_agregan_dos_libros_a_sus_libros(self):
    biblioteca = Biblioteca()
    biblioteca.agregar_libro("Socorro")
    biblioteca.agregar_libro("El lobo estepario")
    self.assertEqual(biblioteca.libros, ["Socorro", "El lobo estepario"])
    
  