from random import choices
try:
    from get_module import get_info
except:
    from .get_module import get_info

def get_species(id):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{id}/"
    return get_info(url)

def preevolucion(dict_species):
    if dict_species['evolves_from_species'] != None:
        resultado = dict_species['evolves_from_species']['name'].capitalize()
    else:
        resultado = None
    return resultado

def indicadores(indicador, dict_species):
    """
    indicador: 'baby': Bebé, 'legendary': Legendario, 'mythical': Mítico.
    """
    resultado = dict_species[f'is_{indicador}']
    return resultado

def descripciones(dict_species):
    descripciones = [entrada['flavor_text'].replace('\n', ' ') for entrada in dict_species['flavor_text_entries'] if entrada['language']['name'] == 'es']
    resultado = choices(descripciones)[0]
    return resultado


if __name__ == '__main__':
    from get_base_info import poke_num, get_base_pokemon
    nombre = 'pichu'
    dict_base_pokemon = get_base_pokemon(nombre)
    id = poke_num(dict_base_pokemon)
    dict_species = get_species(id)
    
    print(f"Datos de {nombre.capitalize()}:")
    print(f"La etapa previa del pokémon es {preevolucion(dict_species)}.")
    print(f"¿Es Bebé este pokémon? {indicadores('baby', dict_species)}.")
    print(f"¿Es Legendario este pokémon? {indicadores('legendary', dict_species)}.")
    print(f"¿Es Mítico este pokémon? {indicadores('mythical', dict_species)}.")
    print(descripciones(dict_species))

    print(indicadores('baby', dict_species), type(indicadores('baby', dict_species)))