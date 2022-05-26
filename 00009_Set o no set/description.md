Hasta acá usamos dos tipos de colecciones, las listas y los diccionarios. Ahora vamos a conocer los **sets** (en castellano conjuntos).

Los sets son muy parecidos a las listas, pero tienen dos particularidades que los diferencian:

* no tienen elementos repetidos;
* sus elementos no están ordenados.

¡Vamos a probarlos en acción! :nerd:

Dado el siguiente código…

```python
ム set_vacio = set()
ム un_set = set([1,2,3,4])
ム otro_set = set([1,2,3,1,2,3])
```

> … probá en la consola lo siguiente en orden:
>
>``` python
ム set_vacio
```
>
>``` python
ム un_set
```
>
>``` python
ム otro_set
```
>
>``` python
ム otro_set.issubset(un_set)
```
>
>``` python
ム un_set.issubset(otro_set)
```
>
>``` python
ム set_vacio.add("hola")
```
>
>``` python
ム set_vacio
```
>
>``` python
ム un_set.remove(4)
```
>
>``` python
ム un_set
```
>
>``` python
ム un_set.clear()
```
>
>``` python
ム un_set
```
>
>``` python
ム un_set.add(5)
```
>
>``` python
ム un_set
```
> ¿Te imaginás que pasará en cada caso? :thought_balloon: