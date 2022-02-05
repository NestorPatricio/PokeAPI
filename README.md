# PokeAPI
😲A web app with information about Pokémon, as a Pokédex.

💻El repositorio corresponde a un desafío evaluado del módulo **Fundamentos de programación en Python**, parte del bootcamp **Desarrollo de aplicaciones *full stack* Python trainee 2021** de **[Edutecno](https://edutecno.cl/)**. La idea es practicar conceptos de *funciones* y de *modularización* del código.
#
⌨Las instrucciones generales son las siguientes:
- **El Pokedex** era el dispositivo que todo maestro pokemon llevaba consigo para consultar acerca de los pokemones que encontraban. Esta Pokédex entrega mucha información útil acerca del Pokemón.
- Afortunadamente, los fanáticos del mundo han creado la [PokeAPI](https://pokeapi.co): un repositorio de toda la información disponible del mundo Pokemon. Con esta información crearemos nuestra propia versión de la Pokédex.
- Ir a la página de la [PokéAPI](https://pokeapi.co/) y chequear la documentación referente a:
  * [Pokemones](https://pokeapi.co/docs/v2#pokemon).
  * [Species](https://pokeapi.co/docs/v2#pokemon-species).
  * [Tipos](https://pokeapi.co/docs/v2#types).
- La información requerida para hacer la Pokédex es la siguiente:
  + Nombre y Número (id) del Pokemón.
  + Peso y altura.
  + Etapa previa, si es que está disponible.
  + Estadísticas (HP, ataque, defensa, etc).
  + Tipo. Notar que un Pokémon sólo puede tener 1 o 2 tipos.
  + Indicadores Especiales. Esta información debe ser agregada en caso de tener alguno de estos Indicadores:
    - Mítico.
    - Legendario.
    - Bebé.
  + Una descripción. La API posee muchas descripciones para cada Pokémon, basta con utilizar una de ellas escogida al azar. La idea es que si se llama distintas veces al mismo pokémon se utilicen distintas descripciones (pero sólo en español).
  + Fortalezas y Debilidades.

- El código final debe cumplir las siguientes indicaciones:
  + Todos los ingresos de datos deben validarse, si un nombre de pokemon no válido se ingresa la API no debe fallar, sino que se debe colocar un mensaje para ingresar un nombre válido (se provee este código).
  + Para la App se solicitará que el usuario ingrese los valores separados por “-” y sin signos de puntuación. Se recomienda un mensaje de este tipo:
  +     “Nota: Si el pokémon tiene espacios reemplace por "-". No coloque ningún tipo de signo de puntuación adicional. Ejemplo: Mr. Mime, se debe ingresar como mr-mime o Mr-Mime.”
  + Las fotos a mostrar deben ser las del art-work official de frente. Las fotos pueden encontrarse en “sprites”.
  + Las descripciones pueden encontrarse en `flavor_text`. Tener especial cuidado de utilizar sólo las que están en español (es).
  + Las fortalezas y resistencias pueden encontrarse en `damage_relations`. Usar los ejemplos para referirse a los campos correctos.
  + Los resultados del Pokedex deben mostrarse directamente en el Pokedex.
  + Se considerarán sólo 898 pokemones. Megaevoluciones y Gigamax no serán parte del problema.
#
La investigación de la API se realizó con la aplicación de escritorio **[Postman](https://www.postman.com/)** v.9.13.0.\
El proyecto final se encuentra en la siguiente página de **[GitHub](https://github.com/NestorPatricio/PokeAPI)**.

Desde el ocio, **[Néstor Patricio Rojas Ríos](https://github.com/NestorPatricio)**

🤘🏽 _Enjoy it!_
