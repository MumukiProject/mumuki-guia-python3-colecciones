El uso más común de las tuplas es cuando queremos retornar más de una cosa y sabemos exactamente cuántas. Recordemos que las funciones o los métodos con retorno solo pueden retornar un valor, pero ¿y si ese valor es una tupla? :wink:

Analicemos un ejemplo para que sea más claro. Supongamos que tenemos una clase `Radio` con un método que nos dice cual es la estación anterior y cuál la siguiente que puede sintonizar. La misma podría estar definida así:

```python
class Radio:
	def __init__(self, estacion):
		self.estacion_actual = estacion

	def anterior_y_siguiente(self):
		return (self.estacion_actual - 0.2, self.estacion_actual + 0.2)
```

De esta forma, estamos obteniendo las dos estaciones pero solo estamos retornando un valor ¡una tupla! :raised_hands:

¡Ahora te toca a vos!

> Definí en la clase `Persona`, el método `iniciales` que nos retorne una tupla con la primera letra del nombre, la primera letra del segundo nombre y la letra del apellido.
>
```python
ム borges = Persona("Jorge", "Luis", "Borges")
ム borges.iniciales()
("J", "L", "B")
```