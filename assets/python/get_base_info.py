# Dada la organización en diferentes carpetas, la siguiente importación presenta 2 alternativas:
# La primera (en "try"), una importación absoluta, permite correr el código desde este script.
# La segunda forma (en "except"), una importación relativa, permite que el código corra desde un script que se encuentra en otra carpeta.
try:
    from get_module import get_info
except:
    from .get_module import get_info

def get_base_pokemon(name: str):
    """
    name: un string con el nombre del pokémon a evaluar.\n
    Retorna una estructura de datos de Python (en este caso, diccionario) con la información básica del pokémon.
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
    return get_info(url)

# Las siguientes funciones obtienen su información del diccionario generado con get_base_pokemon().
# De esta forma, evitamos hacer una nueva solictud GET cada vez que requerimos una información.
def poke_name(dict_base_pokemon: dict):
    """
    dict_base_pokemon: estructura de datos de la cual se obtiene la información.\n
    Accede hasta el nivel: API['name'].
    Excepción: si el nombre es 'type-null' asigna automáticamente 'Código Cero'.\n
    Retorna el nombre del pokémon con las primeras letras en mayúscula.
    """
    if dict_base_pokemon['name'] == "type-null":
        respuesta = "Código Cero"
    else:
        respuesta = dict_base_pokemon['name'].title()
    return respuesta

def poke_num(dict_base_pokemon: dict):
    """
    dict_base_pokemon: estructura de datos de la cual se obtiene la información.\n
    Accede hasta el nivel: API['id'].\n
    Retorna el número del pokémon, según la Pokédex Nacional.
    """
    respuesta = str(dict_base_pokemon['id'])
    return respuesta

def poke_weight(dict_base_pokemon: dict):
    """
    dict_base_pokemon: estructura de datos de la cual se obtiene la información.\n
    Accede hasta el nivel: API['weight'].\n
    Retorna el peso del pokémon en kilogramos.
    """
    respuesta = str((dict_base_pokemon['weight'] / 10)).replace('.', ',')
    return respuesta

def poke_height(dict_base_pokemon: dict):
    """
    dict_base_pokemon: estructura de datos de la cual se obtiene la información.\n
    Accede hasta el nivel: API['height'].\n
    Retorna la altura del pokémon en metros.
    """
    respuesta = str((dict_base_pokemon['height'] / 10)).replace('.', ',')
    return respuesta

def poke_stats(caracter: int, dict_base_pokemon: dict):
    """
    caracter: 0: HP, 1: Ataque, 2: Defensa, 3: Ataque Esp, 4: Defensa Esp, 5: Velocidad.
    dict_base_pokemon: estructura de datos de la cual se obtiene la información.\n
    Accede hasta el nivel: API['stats'][n(caracter)]['base_stat'].\n
    Retorna el valor del atributo definido en "caracter" para un determinado pokémon.
    """
    respuesta = str(dict_base_pokemon['stats'][caracter]['base_stat'])
    return respuesta

def poke_type(dict_base_pokemon: dict):
    """
    dict_base_pokemon: estructura de datos de la cual se obtiene la información.\n
    Accede hasta el nivel: API['types'][n(tipo)]['type']['url].\n
    Retorna una lista con las direcciones web de la API con la información de los tipos del pokémon.
    """
    respuesta = [tipo['type']['url'] for tipo in dict_base_pokemon['types']]
    return respuesta

def poke_photo(dict_base_pokemon):
    """
    dict_base_pokemon: estructura de datos de la cual se obtiene la información.\n
    Accede hasta el nivel: API['id'].\n
    Retorna la dirección web donde se encuentra la imagen fan art del pokémon.
    """
    respuesta = f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{dict_base_pokemon["id"]}.png'
    return respuesta


if __name__ == '__main__':
    nombre = 'clefairy'
    dict_base_pokemon = get_base_pokemon(nombre)
    
    print(f"El nombre del pokémon es {poke_name(dict_base_pokemon)}.")
    print(f"El número del pokémon, según la Pokédex Nacional, es {poke_num(dict_base_pokemon)}.")
    print(f"El peso del pokémon es de {poke_weight(dict_base_pokemon)} kilos.")
    print(f"La altura del pokémon es de {poke_weight(dict_base_pokemon)} metros.")
    print(f"El HP del pokémon es de {poke_stats(0, dict_base_pokemon)}.")
    print(f"El ataque del pokémon es de {poke_stats(1, dict_base_pokemon)}.")
    print(f"La defensa del pokémon es de {poke_stats(2, dict_base_pokemon)}.")
    print(f"El ataque especial del pokémon es de {poke_stats(3, dict_base_pokemon)}.")
    print(f"La defensa especial del pokémon es de {poke_stats(4, dict_base_pokemon)}.")
    print(f"La velocidad del pokémon es de {poke_stats(5, dict_base_pokemon)}.")
    print(f"Los tipos del pokémon están en {poke_type(dict_base_pokemon)}.")
    print(f"La imagen del pokémon está en {poke_photo(dict_base_pokemon)}.")
