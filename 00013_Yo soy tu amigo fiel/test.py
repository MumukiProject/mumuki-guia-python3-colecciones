
  def test_Un_juguete_con_precio_minorista_menor_a_1000_y_precio_mayorista_menor_a_600_es_barato(self):
    buzz = Juguete("Buzz Lightyear", 800, 500, set([{"pieza": "cabeza", "tamaño": "grande"}, {"pieza": "cuerpo", "tamaño": "grande"})
    self.assertTrue(buzz.es_barato())
    
    
    

#  Un juguete con precio minorista menor a 1000 y precio mayorista menor a 600 es barato.
#Un juguete con precio minorista mayor a 1000 y precio mayorista menor a 600 no es barato.
#Un juguete con precio minorista menor a 1000 y precio mayorista mayor a 600 no es barato.
#precios_con_iva de un juguete con precio minorista XX y mayorista YY retorna la tupla (ZZ, TT).
#precios_con_iva de un juguete con precio minorista XX y mayorista YY retorna la tupla (ZZ, TT).
#Un juguete que tiene todas partes grandes es apto para todo público.
#Un juguete que tiene alguna parte que no es grande no es apto para todo público.

