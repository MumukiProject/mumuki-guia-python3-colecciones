Ya vimos 3 tipos de colecciones: las listas, los diccionarios y los sets. Solo nos queda uno por ver, las **tuplas**. Las tuplas son similares a las listas pero tienen una particularidad, son inmutables. En criollo, las tuplas no se pueden modificar por lo que:

* no podemos agregarles ni quitarles elementos;
* no podemos modificar el valor de sus elementos. 

Es por este motivo que las tuplas se utilizan en aquellos casos donde quisiéramos usar una lista pero ya sabemos de antemano cuántos y qué elementos va a tener. 

Las tuplas se pueden representar de tres formas:

```python
ム tupla_1 = ("Violeta", "Amarillo")
ム tupla_2 = "Naranja", "Azul"
ム tupla_3 = tuple(22, 22, True)
```

> Veamos qué podemos hacer (y qué no) probando lo siguiente en la consola:
>
```python
ム tupla_1
ム tupla_2
ム tupla_3
ム tupla_1[0]
ム tupla_3[2]
ム tupla_2[2]
ム len(tupla_1)
ム len(tupla_3)
ム tupla_3[2] = False
```