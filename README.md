# PokeAPI
馃槻A web app with information about Pok茅mon, as a Pok茅dex.

馃捇El repositorio corresponde a un desaf铆o evaluado del m贸dulo **Fundamentos de programaci贸n en Python**, parte del bootcamp **Desarrollo de aplicaciones *full stack* Python trainee 2021** de **[Edutecno](https://edutecno.cl/)**. La idea es practicar conceptos de *funciones* y de *modularizaci贸n* del c贸digo.
#
鈱↙as instrucciones generales son las siguientes:
- **El Pokedex** era el dispositivo que todo maestro pokemon llevaba consigo para consultar acerca de los pokemones que encontraban. Esta Pok茅dex entrega mucha informaci贸n 煤til acerca del Pokem贸n.
- Afortunadamente, los fan谩ticos del mundo han creado la [PokeAPI](https://pokeapi.co): un repositorio de toda la informaci贸n disponible del mundo Pokemon. Con esta informaci贸n crearemos nuestra propia versi贸n de la Pok茅dex.
- Ir a la p谩gina de la [Pok茅API](https://pokeapi.co/) y chequear la documentaci贸n referente a:
  * [Pokemones](https://pokeapi.co/docs/v2#pokemon).
  * [Species](https://pokeapi.co/docs/v2#pokemon-species).
  * [Tipos](https://pokeapi.co/docs/v2#types).
- La informaci贸n requerida para hacer la Pok茅dex es la siguiente:
  + Nombre y N煤mero (id) del Pokem贸n.
  + Peso y altura.
  + Etapa previa, si es que est谩 disponible.
  + Estad铆sticas (HP, ataque, defensa, etc).
  + Tipo. Notar que un Pok茅mon s贸lo puede tener 1 o 2 tipos.
  + Indicadores Especiales. Esta informaci贸n debe ser agregada en caso de tener alguno de estos Indicadores:
    - M铆tico.
    - Legendario.
    - Beb茅.
  + Una descripci贸n. La API posee muchas descripciones para cada Pok茅mon, basta con utilizar una de ellas escogida al azar. La idea es que si se llama distintas veces al mismo pok茅mon se utilicen distintas descripciones (pero s贸lo en espa帽ol).
  + Fortalezas y Debilidades.

- El c贸digo final debe cumplir las siguientes indicaciones:
  + Todos los ingresos de datos deben validarse, si un nombre de pokemon no v谩lido se ingresa la API no debe fallar, sino que se debe colocar un mensaje para ingresar un nombre v谩lido (se provee este c贸digo).
  + Para la App se solicitar谩 que el usuario ingrese los valores separados por 鈥?-鈥? y sin signos de puntuaci贸n. Se recomienda un mensaje de este tipo:
  +     鈥淣ota: Si el pok茅mon tiene espacios reemplace por "-". No coloque ning煤n tipo de signo de puntuaci贸n adicional. Ejemplo: Mr. Mime, se debe ingresar como mr-mime o Mr-Mime.鈥?
  + Las fotos a mostrar deben ser las del art-work official de frente. Las fotos pueden encontrarse en 鈥渟prites鈥?.
  + Las descripciones pueden encontrarse en `flavor_text`. Tener especial cuidado de utilizar s贸lo las que est谩n en espa帽ol (es).
  + Las fortalezas y resistencias pueden encontrarse en `damage_relations`. Usar los ejemplos para referirse a los campos correctos.
  + Los resultados del Pokedex deben mostrarse directamente en el Pokedex.
  + Se considerar谩n s贸lo 898 pokemones. Megaevoluciones y Gigamax no ser谩n parte del problema.
#
La investigaci贸n de la API se realiz贸 con la aplicaci贸n de escritorio **[Postman](https://www.postman.com/)** v.9.13.0.\
El proyecto final se encuentra en la siguiente p谩gina de **[GitHub](https://github.com/NestorPatricio/PokeAPI)**.

Desde el ocio, **[N茅stor Patricio Rojas R铆os](https://github.com/NestorPatricio)**

馃馃徑 _Enjoy it!_
