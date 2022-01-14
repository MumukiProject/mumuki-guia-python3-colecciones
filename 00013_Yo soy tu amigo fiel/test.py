
  def test_Un_juguete_con_precio_minorista_menor_a_1000_y_precio_mayorista_menor_a_600_es_barato(self):
    buzz = Juguete("Buzz Lightyear", 800, 500, set([{"pieza": "cabeza", "tamaño": "grande"}, {"pieza": "cuerpo", "tamaño": "grande"}])
    self.assertTrue(buzz.es_barato())
