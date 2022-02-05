from random import choices
# Dada la organización en diferentes carpetas, la siguiente importación presenta 2 alternativas:
# La primera (en "try"), una importación absoluta, permite correr el código desde este script.
# La segunda forma (en "except"), una importación relativa, permite que el código corra desde un script que se encuentra en otra carpeta.
try:
    from get_module import get_info
except:
    from .get_module import get_info

def get_species(id: str):
    """
    id: el número del pokémon a evaluar, según la Pokédex Nacional.\n
    Retorna una estructura de datos de Python (en este caso, diccionario) con la información complementaria del pokémon.
    """
    url = f"https://pokeapi.co/api/v2/pokemon-species/{id}/"
    return get_info(url)

# Las siguientes funciones obtienen su información del diccionario generado con get_species().
# De esta forma, evitamos hacer una nueva solictud GET cada vez que requerimos una información.
def preevolucion(dict_species: dict):
    """
    dict_species: estructura de datos de la cual se obtiene la información.\n
    Accede hasta el nivel: API['evolves_from_species']['name'].
    Excepción: si el pokémon no tiene pre-evolución, se entrega un valor None.\n
    Retorna, el nombre de la pre-evolución del pokémon, con las primeras letras en mayúscula, o None.
    """
    if dict_species['evolves_from_species'] != None:
        resultado = dict_species['evolves_from_species']['name'].capitalize()
    else:
        resultado = None
    return resultado

def indicadores(indicador: str, dict_species: dict):
    """
    indicador: 'baby': Bebé, 'legendary': Legendario, 'mythical': Mítico.
    dict_species: estructura de datos de la cual se obtiene la información.\n
    Accede hasta el nivel: API['is_(indicador)'].\n
    Retorna un booleano: True si el pokémon tiene el indicador, False si no lo tiene.
    """
    resultado = dict_species[f'is_{indicador}']
    return resultado

def descripciones(dict_species: dict):
    """
    dict_species: estructura de datos de la cual se obtiene la información.\n
    Accede hasta el nivel: API['flavor_text_entries'][n]['flavor_text'].
    Dentro, se genera una lista con todas las descripciones posibles, y escoge una.
    Excepción: sólo integran la lista las descripciones cuyo valor de API['flavor_text_entries'][n]['language']['name'] sea igual a 'es'.\n
    Retorna una de las posibles breves descripciones, en español, del pokémon.
    """
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