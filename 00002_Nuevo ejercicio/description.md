Refactorizar el método del ejercicio anterior contando que las listas son objetos y que los procedimientos y funciones que veníamos utilizando con ellas también se pueden escribir como métodos. list.append(atributo, elemento) => atributo.append(elemento).

# Ejercicio 2

class Biblioteca:
  def __init__(self):
    self.libros = []

  def agregar_libro(self, libro):
    self.libros.append(libro)