  
  def test_Si_a_una_biblioteca_con_tres_libros_largos_le_enviamos_el_mensaje_libros_largos_nos_retorna_esos_tres_libros(self):
    biblioteca = Biblioteca()
    self.assertEqual(biblioteca.libros, ["Socorro", "El lobo estepario"])
    
    def test_un_libro_con_menos_de_300_paginas_no_es_largo(self):
    un_libro_corto = Libro("Socorro", 299, "Terror")
    self.assertFalse(un_libro_corto.es_largo())

  def test_un_libro_con_300_paginas_no_es_largo(self):
    otro_libro_corto = Libro("Fundación", 300, "Ciencia ficción")
    self.assertFalse(otro_libro_corto.es_largo())

  def test_un_libro_con_mas_de_300_paginas_es_largo(self):
    otro_libro_corto = Libro("Fundación e imperio", 301, "Ciencia ficción")
    self.assertTrue(otro_libro_corto.es_largo())