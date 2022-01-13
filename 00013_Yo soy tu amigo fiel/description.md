Para ir terminando esta lección vamos a jugar un poco. Bah, en realidad no, pero vamos a hacer algo parecido. Vamos a modelar juguetes. :race_car:

De estos juguetes sabremos el nombre, su precio minorista, su precio mayorista y las partes que lo componen. Estas partes estarán representadas por un set de diccionarios donde cada diccionario está compuesto por el nombre de una pieza y el tamaño que tiene. Por ejemplo:

```python
autito = Juguete("Relámpago marquinhos", 400, 300, set([{"pieza": "carcaza", "tamaño": "grande"}, {"pieza": "rueda_1", "tamaño": "chica"}, {"pieza": "rueda_2", "tamaño": "chica"}, {"pieza": "rueda_3", "tamaño": "chica"}, {"pieza": "rueda_4", "tamaño": "chica"}])
```

Si bien la clase ya está creada con su constructor debemos definir algunos métodos:

* `es_barato` que nos dice si el `precio_minorista` es menor a 1000 y el `precio_mayorista` es menor a 600;
* `precios_con_iva` que retorna una tupla con el precio minorista y el mayorista con su IVA (multiplicados por 1.21);
* `es_apto_para_todo_publico` que se cumple solo si todas sus partes son tienen un tamaño `"grande"`.

> Definí los métodos solicitados en la clase `Juguete`.