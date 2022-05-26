Ya conocimos tres tipos de colecciones: las listas, los diccionarios y los sets. Solo nos queda uno por descubrir, las **tuplas**. Las tuplas son similares a las listas pero tienen una particularidad, son inmutables. En criollo, las tuplas no se pueden modificar por lo que:

* no podemos agregarles ni quitarles elementos;
* no podemos modificar el valor de sus elementos.

Es por este motivo que las tuplas se utilizan en aquellos casos donde quisiéramos usar una lista pero ya sabemos de antemano cuántos y qué elementos va a tener. 

Las tuplas se pueden representar de tres formas:

```python
ム tupla_1 = ("Violeta", "Amarillo")
ム tupla_2 = "Naranja", "Azul"
ム tupla_3 = tuple((22, 22, True))
```

> Para saber qué podemos hacer (y qué no) probemos lo siguiente en la consola en orden:
>
>```python
ムtupla_1
```
>
>```python
ムtupla_2
```
>
>```python
ムtupla_3
```
>
>```python
ムtupla_1[0]
```
>
>```python
ムtupla_3[2]
```
>
>```python
ムtupla_2[2]
```
>
>```python
ムlen(tupla_1)
```
>
>```python
ムlen(tupla_2)
```
>
>```python
ムlen(tupla_3)
```
>
>```python
ムtupla_3[2] = False
```