El uso más común de las tuplas es cuando queremos retornar más de una cosa y sabemos exactamente cuántas. Recordemos que las funciones solo retornan un valor, pero ¿y si ese valor es una tupla? :wink:

Veámoslo con un ejemplo para que sea más claro. Supongamos que tenemos una función que a partir de una palabra nos diga cuál es su primera y su última letra. La misma podría estar definida de esta forma:

```python
def primera_y_última_letra(palabra):
	return (palabra[0], palabra[len(palabra) - 1])
```

De esta forma estamos obteniendo la primera letra y la última pero solo estamos retornando un valor ¡la tupla compuesta por esas dos letras! :raised_hands:

¡Ahora te toca a vos!

> Definí una función `anterior_y_siguiente` que a partir de un número entero retorne una tupla con el número anterior y el número siguiente:
>
```python
ム anterior_y_siguiente(8)
(7, 9)
>
ム anterior_y_siguiente(4)
(3, 5)
````