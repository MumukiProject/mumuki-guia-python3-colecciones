Para ir terminando esta lección vamos a jugar un poco. Bah, en realidad no, pero vamos a hacer algo parecido. Vamos a modelar juguetes. :race_car:

De estos juguetes sabremos el nombre, su precio minorista, su precio mayorista y las partes que lo componen. Por ejemplo:

```python
autito = Juguete("Relámpago Marquinhos", 400, 300, set(["ruedas", "carcaza", "batería"])

pinocho = Juguete("Pinocho", 500, 420, set(["cuerpo", "ropa", "cuerda"]))
```

Si bien la clase ya está creada con su constructor debemos definir algunos métodos:

* `es_barato` que nos dice si el `precio_minorista` es menor a 1000 y el `precio_mayorista` es menor a 600;
* `precios_con_iva` que retorna una tupla con el precio minorista y el mayorista con su IVA (multiplicados por 1.21);
* `es_electronico` que se cumple si tiene `"batería"` entre sus elementos.

> Definí los métodos solicitados en la clase `Juguete`.