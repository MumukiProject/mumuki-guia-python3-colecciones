
  def setUp(self):
    self.pizarra_magica = Juguete("Pizarra mágica", 1001, 599, set(["pizarra", "lápiz"]))
    self.buzz = Juguete("Buzz Lightyear", 800, 500, set(["cuerpo", "traje", "batería", "bateria"]))
    self.auto = Juguete("Auto control remoto", 900, 550, set(["ruedas", "carcaza", "batería", "bateria"]))
    self.muneca = Juguete("Muñeca", 1200, 550, set(["cuerpo", "ropa"]))
    
  def test_una_jugueteria_inicialmente_no_tiene_juguetes(self):
    jugueteria = Jugueteria()
    self.assertEqual(jugueteria.productos, [])
    
  def test_cuando_la_jugueteria_adquiere_un_producto_el_mismo_se_agrega_a_su_lista_de_productos(self):
    jugueteria = Jugueteria()
    jugueteria.adquirir_producto(self.buzz)
    self.assertEqual(jugueteria.productos, [self.buzz])
    
  def test_cuando_la_jugueteria_adquiere_dos_productos_los_mismo_se_agregan_a_su_lista_de_productos(self):
    jugueteria = Jugueteria()
    jugueteria.adquirir_producto(self.buzz)
    jugueteria.adquirir_producto(self.auto)
    self.assertEqual(jugueteria.productos, [self.buzz, self.auto])

  def test_el_catalogo_de_oferta_de_una_jugueteria_retorna_los_nombres_de_los_productos_baratos_de_la_lista(self):
    jugueteria = Jugueteria()
    jugueteria.adquirir_producto(self.auto)
    jugueteria.adquirir_producto(self.buzz)
    jugueteria.adquirir_producto(self.pizarra_magica)
    self.assertEqual(jugueteria.catalogo_de_oferta(), ["Auto control remoto", "Buzz Lightyear"])

  def test_el_catalogo_de_oferta_de_una_jugueteria_retorna_la_lista_vacia_si_no_tiene_productos(self):
    jugueteria = Jugueteria()
    self.assertEqual(jugueteria.catalogo_de_oferta(), [])

  def test_el_catalogo_de_oferta_de_una_jugueteria_retorna_la_lista_vacia_si_ningun_producto_es_barato(self):
    jugueteria = Jugueteria()
    jugueteria.adquirir_producto(self.pizarra_magica)
    jugueteria.adquirir_producto(self.muneca)
    self.assertEqual(jugueteria.catalogo_de_oferta(), [])
