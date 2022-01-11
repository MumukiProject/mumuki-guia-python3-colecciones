  
  def test_Si_a_una_biblioteca_con_tres_libros_largos_le_enviamos_el_mensaje_libros_largos_nos_retorna_esos_tres_libros(self):
    biblioteca = Biblioteca()
    biblioteca.agregar_libro("Socorro")
    biblioteca.agregar_libro("El lobo estepario")
    self.assertEqual(biblioteca.libros, ["Socorro", "El lobo estepario"])