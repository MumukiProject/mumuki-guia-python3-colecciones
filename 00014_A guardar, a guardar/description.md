Ahora que tenemos los juguetes solo nos resta modelar a las jugueterías :bear:. De ellas sabemos qué:

* tienen una lista de `productos` que inicialmente está vacía;
* entienden el mensaje `adquirir_producto` que agrega un producto a esa colección;
* al enviarles el mensaje `catalogo_de_oferta` retornan el nombre de aquellos productos que son baratos.


Teniendo en cuenta que los `productos` son juguetes, nuestro diagrama de clases sería este:

<img src="https://raw.githubusercontent.com/MumukiProject/mumuki-guia-python3-colecciones/master/assets/clases_5_1648656529453.13.svg" alt="clases_5_1648656529453.13.svg" width="450" height="auto">


> Definí la clase `Jugueteria` con los métodos `__init__`, `adquirir_producto` y `catalogo_de_oferta`.