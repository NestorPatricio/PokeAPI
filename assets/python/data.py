# Objetos tipo string que se usan en distintos procesos del código.

validacion_pokemon = "La opción ingresada no es válida. Por favor, escriba el nombre correctamente: "

MENU = """¡Bienvenido a PokéAPI! 
¡Este mundo está habitado por unas criaturas llamadas POKÉMON!
Para algunos, los POKÉMON son mascotas. Pero otros los usan para pelear.
En cuanto a mí... Estudio a los POKÉMON como profesión, y me encargo de compartir ese conocimiento.
Pero primero dime ¿Te gustaría investigar más de los POKÉMON?

1. ¡Claro que me gustaría, adelante!
0. Por el momento paso, gracias.

> """

ELECCION = """Escribe el nombre del POKÉMON que quieras conocer.
Por favor, no uses acentos ni signos de puntuación.
Si el nombre del POKÉMON tiene espacios, reemplázalo por un signo '-'.
Por ejemplo, para buscara a Mr. Mime debes escribir: 'Mr-Mime'.

> """

ESPERA = f"""Interesante elección.
Espera un poco mientras busco la información.
"""

TIPOS = {
    'normal': 'normal',
    'fighting': 'lucha',
    'flying': 'volador',
    'poison': 'veneno',
    'ground': 'tierra',
    'rock': 'roca',
    'bug': 'bicho',
    'ghost': 'fantasma',
    'steel': 'acero',
    'fire': 'fuego',
    'water': 'agua',
    'grass': 'planta',
    'electric': 'eléctrico',
    'psychic': 'psíquico',
    'ice': 'hielo',
    'dragon': 'dragón',
    'dark': 'siniestro',
    'fairy': 'hada'
}