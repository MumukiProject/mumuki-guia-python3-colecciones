Ejercicio para hacer varias instanciaciones de estos objetos con las estructuras de datos

# Ejercicio 7

carl_sagan = {"nombre": "Carl", "apellido": "Sagan", "nacionalidad": "Estados Unidos" }
contacto = Libro("Contacto", 400, "Ciencia Ficción", carl_sagan)

elsa_bornemann = {"nombre": "Elsa", "apellido": "Bornemann", "nacionalidad": "Argentina" }
socorro = Libro("Socorro", 250, "Terror", elsa_bornemann)

biblioteca_de_ofelia = Biblioteca()
biblioteca_de_ofelia.agregar_libro(contacto)
biblioteca_de_ofelia.agregar_libro(socorro)


