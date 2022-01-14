
  def test_un_juguete_con_precio_minorista_mayor_a_1000_y_precio_mayorista_menor_a_600_no_es_barato(self):
    pizarra_magica = Juguete("Pizarra mágica", 1001, 599, set([{"pieza": "pizarra", "tamaño": "grande"}]))
    self.assertFalse(pizarra_magica.es_barato())
