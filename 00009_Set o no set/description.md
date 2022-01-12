Hasta acá vimos dos tipos de colecciones, las listas y los diccionarios. Vamos a conocer los **sets** (en castellano conjuntos).

Los sets son muy parecidos a las listas pero tienen dos particularidades que los diferencian:

* no tienen elementos repetidos;
* sus elementos no están ordenados.

¡Vamos a verlos en acción! :nerd:

Dado el siguiente código…

```python
ム set_vacio = set()
ム un_set = set([1,2,3,4])
ム otro_set = set([1,2,3,1,2,3])
```

> … probá en la consola lo siguiente:
>
```python
ム set_vacio
ム un_set
ム otro_set
ム otro_set.issubset(un_set)
ム un_set.issubset(otro_set)
ム set_vacio.add("hola")
ム set_vacio
ム un_set.remove(4)
ム un_set
ム un_set.clear()
ム un_set
```
> ¿Te imaginás que pasará en cada caso? :thought_balloon: