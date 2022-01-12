
  def test_la_biblioteca_de_emma_tiene_los_libros_contacto_y_socorro(self):
    self.assertEqual(biblioteca_de_emma.libros, [contacto, socorro])
  
  def test_contacto_tiene_de_titulo_contacto(self):
    self.assertEqual(contacto.titulo.lower(), "contacto")
    
  def test_contacto_tiene_400_paginas(self):
    self.assertEqual(contacto.paginas, 400)
    
  def test_contacto_es_un_libro_de_ciencia_ficcion(self):
    genero = contacto.genero.lower()
    self.assertTrue(genero == 'ciencia ficcion' or genero == 'ciencia ficción', "El género de contacto debería ser ciencia ficción")
    
  def test_el_escritor_de_contacto_se_llama_carl(self):
    self.assertEqual(contacto.artista["nombre"].lower(), "carl")
    
  def test_el_escritor_de_contacto_se_apellida_sagan(self):
    self.assertEqual(contacto.artista["apellido"].lower(), "sagan")
    
  def test_el_escritor_de_contacto_es_de_estados_unidos(self):
    self.assertEqual(contacto.artista["nacionalidad"].lower(), "estados unidos")
  
  def test_socorro_tiene_de_titulo_socorro(self):
    self.assertEqual(socorro.titulo.lower(), "socorro")
    
  def test_socorro_tiene_250_paginas(self):
    self.assertEqual(socorro.paginas, 250)
    
  def test_socorro_es_un_libro_de_terror(self):
    self.assertEqual(socorro.genero.lower(), "terror")
    
  def test_la_escritora_de_socorro_se_llama_elsa(self):
    self.assertEqual(socorro.artista["nombre"].lower(), "elsa")
    
  def test_la_escritora_de_socorro_se_apellida_bornemann(self):
    self.assertEqual(socorro.artista["apellido"].lower(), "bornemann")
    
  def test_la_escritora_de_socorro_es_de_argentina(self):
    self.assertEqual(socorro.artista["nacionalidad"].lower(), "argentina")