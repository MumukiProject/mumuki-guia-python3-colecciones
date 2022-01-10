Anteriormente, en este recorrido vimos que las listas también son objetos y que entienden sus propios mensajes, ¡aprovechémoslo! :raised_hands:

Queremos modelar bibliotecas con sus libros. Sabemos que al instanciar una biblioteca no tiene libros pero queremos poder agregarle nuevos de esta forma:

```python
ム biblioteca_de_mar = Biblioteca()
ム biblioteca_de_mar.libros
[]
ム biblioteca_de_mar.agregar_libro("La insoportable levedad del ser")
ム biblioteca_de_mar.agregar_libro("Contacto")
ム biblioteca_de_mar.agregar_libro("Historias de cronopios y de famas")
ム biblioteca_de_mar.libros
["La insoportable levedad del ser", "Contacto", "Historias de cronopios y de famas"]
```

> Definí la clase `Biblioteca` de forma tal que entienda el mensaje `agregar_libro`. No te olvides del constructor que inicialice el atributo `libros` como una lista vacía.
