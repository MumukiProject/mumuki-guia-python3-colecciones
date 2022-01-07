Modelar otra clase que tenga colecciones dentro del dominio del ejercicio anterior.

class Jugueteria:
  def __init__(self):
    self.productos = [] # una lista

  def adquirir_producto(self, producto):
    self.productos.append(producto)

  def catalogo_de_oferta(self):
    return [producto.nombre for producto in self.productos if producto.es_barato()]