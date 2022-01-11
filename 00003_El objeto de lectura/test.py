
  def test_si_creo_un_nuevo_Libro_le_puedo_especificar_su_titulo_cantidad_de_páginas_y_género(self):
    un_libro = Libro("Socorro", 250, "Terror")
    self.assertEqual(un_libro.titulo, "Socorro")
    self.assertEqual(un_libro.paginas, 250)
    self.assertEqual(un_libro.genero, "Terror")

  def test_un_libro_con_menos_de_300_paginas_no_es_largo(self):
    un_libro_corto = Libro("Socorro", 299, "Terror")
    self.assertFalse(un_libro_corto.es_largo())

  def test_un_libro_con_300_paginas_no_es_largo(self):
    otro_libro_corto = Libro("Fundación", 300, "Ciencia ficción")
    self.assertFalse(otro_libro_corto.es_largo())

  def test_un_libro_con_mas_de_300_paginas_es_largo(self):
    otro_libro_corto = Libro("Fundación e imperio", 301, "Ciencia ficción")
    self.assertTrue(otro_libro_corto.es_largo())

  def test_una_biblioteca_arranca_sin_libros(self):
    biblioteca = Biblioteca()
    self.assertEqual(biblioteca.libros, [])

  def test_si_una_biblioteca_recibe_el_mensaje_agregar_libro_se_agrega_un_libro_a_sus_libros(self):
    biblioteca = Biblioteca()
    un_libro = Libro("Socorro", 250, "Terror")
    biblioteca.agregar_libro(un_libro)
    self.assertEqual(biblioteca.libros, [un_libro])
