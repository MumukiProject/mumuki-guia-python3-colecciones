
  def setUp(self):
    self.pizarra_magica = Juguete("Pizarra mágica", 1001, 599, set(["pizarra", "lápiz"]))
    self.buzz = Juguete("Buzz Lightyear", 800, 500, set(["cuerpo", "traje", "batería", "bateria"]))
    self.auto = Juguete("Auto control remoto", 900, 700, set(["ruedas", "carcaza", "batería", "bateria"]))
    
  def test_un_juguete_con_precio_minorista_menor_a_1000_y_precio_mayorista_menor_a_600_es_barato(self):
    self.assertTrue(self.buzz.es_barato())
    
  def test_un_juguete_con_precio_minorista_mayor_a_1000_y_precio_mayorista_menor_a_600_no_es_barato(self):
    self.assertFalse(self.pizarra_magica.es_barato())
    
  def test_un_juguete_con_precio_minorista_menor_a_1000_y_precio_mayorista_mayor_a_600_no_es_barato(self):
    self.assertFalse(self.auto.es_barato())

  def test_precios_con_iva_de_un_juguete_con_precio_minorista_800_y_mayorista_500_retorna_la_tupla_con_968_y_605(self):
    self.assertEqual(self.buzz.precios_con_iva(), (968, 605))

  def test_precios_con_iva_de_un_juguete_con_precio_minorista_900_y_mayorista_700_retorna_la_tupla_con_1089_y_847(self):
    self.assertEqual(self.auto.precios_con_iva(), (1089, 847))
  
  def test_un_juguete_que_tiene_bateria_es_electronico(self):
    self.assertTrue(self.buzz.es_electronico())
    
  def test_un_juguete_que_no_tiene_bateria_no_es_electronico(self):
    self.assertFalse(self.pizarra_magica.es_electronico())