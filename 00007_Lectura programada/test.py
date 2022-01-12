
  def la_biblioteca_de_emma_tiene_los_libros_contacto_y_socorro(self):
    self.asserEqual(biblioteca_de_emma.libros, [conctacto, socorro])
  
  def contacto_tiene_de_titulo_contacto(self):
    self.asserEqual(contacto.titulo.lower(), "contacto")
    
  def contacto_tiene_400_paginas(self):
    self.asserEqual(contacto.paginas, 400)
    
  def contacto_es_un_libro_de_ciencia_ficcion(self):
    genero = contacto.genero.lower()
    self.assertTrue(genero == 'ciencia ficcion' or genero == 'ciencia ficción', "El género de contacto debería ser ciencia ficción")
    
  def el_escritor_de_contacto_se_llama_carl(self):
    self.asserEqual(contacto.artista["nombre"].lower(), "carl")
    
  def el_escritor_de_contacto_se_apellida_sagan(self):
    self.asserEqual(contacto.artista["apellido"].lower(), "sagan")
    
  def el_escritor_de_contacto_es_de_estados_unidos(self):
    self.asserEqual(contacto.artista["nacionalidad"].lower(), "estados unidos")
  
  def socorro_tiene_de_titulo_socorro(self):
    self.asserEqual(socorro.titulo.lower(), "socorro")
    
  def socorro_tiene_250_paginas(self):
    self.asserEqual(socorro.paginas, 250)
    
  def socorro_es_un_libro_de_terror(self):
    self.assertEqual(socorro.genero.lower(), "terror")
    
  def la_escritora_de_socorro_se_llama_elsa(self):
    self.asserEqual(socorro.artista["nombre"].lower(), "elsa")
    
  def la_escritora_de_socorro_se_apellida_bornemann(self):
    self.asserEqual(socorro.artista["apellido"].lower(), "bornemann")
    
  def la_escritora_de_socorro_es_de_argentina(self):
    self.asserEqual(socorro.artista["nacionalidad"].lower(), "argentina")