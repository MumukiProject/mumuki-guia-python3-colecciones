
  def test_anterior_y_siguiente_de_10_son_9_y_11(self):
    self.assertEqual(anterior_y_siguiente(10), (9, 11))
    
  def test_anterior_y_siguiente_de_5_son_4_y_6(self):
    self.assertEqual(anterior_y_siguiente(5), (4, 6))
    
  def test_anterior_y_siguiente_de_2_son_1_y_3(self):
    self.assertEqual(anterior_y_siguiente(2), (1, 3))
  
  def test_anterior_y_siguiente_de_7_son_6_y_8(self):
    self.assertEqual(anterior_y_siguiente(7), (6, 8))