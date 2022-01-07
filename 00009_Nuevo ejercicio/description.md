Introducir sets contar sus características. Probar cosas en consola como pedir la posición o agregar un elemento que ya está.

 Ejercicio 9

# Extra code
set_vacio = set()
un_set = set([1,2,3,4])
otro_set = set([1,2,3,1,2,3])

# Para probar en consola
set_vacio
un_set
otro_set
otro_set.issubset(un_set)
un_set.issubset(otro_set)
set_vacio.add("hola")
set_vacio
un_set.remove(4)
un_set
un_set.clear()
un_set

