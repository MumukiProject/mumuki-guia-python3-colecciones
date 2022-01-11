¿Te acordás de las listas por comprensión? :eyes:

Por si acaso repasémoslas. Las listas por comprensión son una herramienta que nos permite hacer mapeos y/o filtrados sobre una lista. Por ejemplo, si quisiéramos obtener el doble de los números mayores a 5 de una lista `numeros` podríamos hacer:

```python
[numero * 2 for numero in numeros if numero > 5]
```

Habiendo recordado esto, vamos a obtener los libros largos de una biblioteca.

> Definí el método `libros_largos` dentro de la clase `Biblioteca` que, utilizando listas por comprensión, nos diga cuáles son sus libros largos.
