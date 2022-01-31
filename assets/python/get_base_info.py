try:
    from get_module import get_info
except:
    from .get_module import get_info

def get_base_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}/"
    return get_info(url)

def poke_name(dict_base_pokemon):
    respuesta = dict_base_pokemon['name'].capitalize()
    return respuesta

def poke_num(dict_base_pokemon):
    respuesta = str(dict_base_pokemon['id'])
    return respuesta

def poke_weight(dict_base_pokemon):
    respuesta = str((dict_base_pokemon['weight'] / 10)).replace('.', ',')
    return respuesta

def poke_height(dict_base_pokemon):
    respuesta = str((dict_base_pokemon['height'] / 10)).replace('.', ',')
    return respuesta

def poke_stats(caracter, dict_base_pokemon):
    """
    caracter: 0: HP, 1: Ataque, 2: Defensa, 3: Ataque Esp, 4: Defensa Esp, 5: Velocidad.
    """
    respuesta = str(dict_base_pokemon['stats'][caracter]['base_stat'])
    return respuesta

def poke_type(dict_base_pokemon):
    respuesta = [tipo['type']['url'] for tipo in dict_base_pokemon['types']]
    return respuesta

def poke_photo(dict_base_pokemon):
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
