
  def test_las_iniciales_de_Jorge_Luis_Borges_son_J_L_y_B(self):
    borges = Persona("Jorge", "Luis", "Borges")
    self.assertEqual(borges.iniciales(), ("J", "L", "B"))
    
  def test_las_iniciales_de_Haydeé_Mercedes_Sosa_son_H_M_y_S(self):
    borges = Persona("Haydée", "Mercedes", "Sosa")
    self.assertEqual(borges.iniciales(), ("H", "M", "S"))
    
  def test_las_iniciales_de_Luis_Alberto_Spinetta_son_L_A_y_S(self):
    borges = Persona("Luis", "Alberto", "Spinetta")
    self.assertEqual(borges.iniciales(), ("L", "A", "S"))