Nuestro programa actual no contiene información de qué artista escribió cada libro. Solucionar ese problema solamente implica agregar un atributo más a nuestra clase `Libro`. Para modelar artistas podemos utilizar otro tipo de colecciones que ya conocemos, ¡los diccionarios!

Los elementos del diccionario que representará a cada artista tendrá como campos su `nombre`, `apellido` y `nacionalidad`. Esta última nos permite también saber la nacionalidad de un libro dado ya que diremos que es la misma que la de la persona que lo escribió.

> Modificá el constructor de la clase `Libro` para que podamos indicarle su `artista` a la hora de instanciar. También definí el método `nacionalidad` en esta clase.