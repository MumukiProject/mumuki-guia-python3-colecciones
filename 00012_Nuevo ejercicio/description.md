Modelar una clase que tenga colecciones.

class Juguete:
  def __init__(self, nombre, precios, partes):
    self.nombre = nombre
    self.precios = precios # una tupla con el precio minorista y el mayorista
    self.partes = partes 
    # set([{"pieza": "brazo", "tamaño": "grande"}, {"pieza": "brazo", "tamaño": "chica"}])
  
  def es_barato(self):
    return self.precios[0] < 1000 and self.precios[1] < 600

  def apto_para_todo_publico(self):
    for parte in partes:
      if parte["tamaño"] == "chica":
        return False
    return True