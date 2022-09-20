Por lo que hicimos en el ejercicio anterior, los libros son strings. Lamentablemente, esto limita bastante nuestro modelado y las cosas que podemos hacer con ellos. :cry:

Por este motivo queremos crear la clase `Libro` :books:, para poder saber no sólo su `titulo` sino también su cantidad de `paginas` y el `genero`. En ese caso, el ejemplo del ejercicio anterior quedaría así:

```python
ム libro_1 = Libro("La insoportable levedad del ser", 330, "Drama")
ム libro_2 = Libro("Contacto", 400, "Ciencia ficción")
ム libro_3 = Libro("Historias de cronopios y de famas", 180, "Ficción")
ム biblioteca_de_mar = Biblioteca()
ム biblioteca_de_mar.libros
[]
ム biblioteca_de_mar.agregar_libro(libro_1)
ム biblioteca_de_mar.agregar_libro(libro_2)
ム biblioteca_de_mar.agregar_libro(libro_3)
```

Y su diagrama de objetos así:

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-colecciones/master/assets/objetos_nuevo2-18_1663684236348.svg" alt="objetos_nuevo2-18_1663684236348.svg" width="700px" height="auto">

> Definí la clase `Libro` con su respectivo constructor. Los libros tienen que entender el mensaje `es_largo` que nos dice si tienen más de 300 `paginas`. ¿Y qué pasa con la clase `Biblioteca`?¿hay que cambiar algo? :eyes: