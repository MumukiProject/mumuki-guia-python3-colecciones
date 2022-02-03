Nuestro programa actual no contiene información sobre quien escribió cada libro. Solucionar ese problema solamente implica agregar un atributo más a nuestra clase `Libro`. Para modelar quién lo escribió podemos utilizar otro tipo de colecciones que ya conocemos, ¡los diccionarios! :star_struck:

Los elementos del diccionario que representará la autoría de un libro tendrá como campos `nombre`, `apellido` y `nacionalidad`. Esta última nos permite también saber la nacionalidad de un libro dado ya que diremos que es la misma que la de la persona que lo escribió. :writing_hand:

> Modificá el constructor de la clase `Libro` para que podamos indicarle su `autoria` a la hora de instanciar. También definí el método `nacionalidad` en esta clase.