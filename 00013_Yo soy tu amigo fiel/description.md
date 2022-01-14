Para ir terminando esta lección vamos a jugar un poco. Bah, en realidad no, pero vamos a hacer algo parecido. Vamos a modelar juguetes. :race_car:

De estos juguetes sabremos el nombre, su precio minorista, su precio mayorista y los materiales con los que está hecho. Por ejemplo:

```python
autito = Juguete("Relámpago Marquinhos", 400, 300, set(["plástico", "metal"])

balero = Juguete("Balero", 150, 80, set(["madera", "hilo"])
```

Si bien la clase ya está creada con su constructor debemos definir algunos métodos:

* `es_barato` que nos dice si el `precio_minorista` es menor a 1000 y el `precio_mayorista` es menor a 600;
* `precios_con_iva` que retorna una tupla con el precio minorista y el mayorista con su IVA (multiplicados por 1.21);
* `es_toxico` que se cumple si tiene `xxxxxx` entre sus materiales.

> Definí los métodos solicitados en la clase `Juguete`.