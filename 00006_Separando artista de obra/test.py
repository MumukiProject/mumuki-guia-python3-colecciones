
  def test_si_creo_un_nuevo_Libro_le_puedo_especificar_su_artista(self):
    un_libro = Libro("Socorro", 250, "Terror", {"nombre": "Elsa", "apellido": "Bornemann", "nacionalidad": "Argentina" })
    self.assertEqual(un_libro.artista, {"nombre": "Elsa", "apellido": "Bornemann", "nacionalidad": "Argentina" })
   
  def test_un_libro_con_una_artista_de_argentina_tiene_nacionalidad_argentina(self):
    un_libro = Libro("Socorro", 299, "Terror", {"nombre": "Elsa", "apellido": "Bornemann", "nacionalidad": "Argentina" })
    self.assertEqual(un_libro.nacionalidad(), "Argentina")

  def test_un_libro_con_una_artista_de_mexico_tiene_nacionalidad_mexico(self):
    un_libro = Libro("Como agua para chocolate", 216, "Realismo mágico", {"nombre": "Laura", "apellido": "Esquivel", "nacionalidad": "México" })
    self.assertEqual(un_libro.nacionalidad(), "México")