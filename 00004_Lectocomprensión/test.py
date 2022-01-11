  
  def test_Si_a_una_biblioteca_con_tres_libros_largos_le_enviamos_el_mensaje_libros_largos_nos_retorna_esos_tres_libros(self):
    biblioteca = Biblioteca()
    biblioteca.libros = [un_libro_largo, segundo_libro_largo, tercer_libro_largo, un_libro_corto]
    self.assertEqual(biblioteca.libros_largos(), [un_libro_largo, segundo_libro_largo, tercer_libro_largo])
