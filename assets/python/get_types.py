# Dada la organización en diferentes carpetas, la siguiente importación presenta 2 alternativas:
# La primera (en "try"), una importación absoluta, permite correr el código desde este script.
# La segunda forma (en "except"), una importación relativa, permite que el código corra desde un script que se encuentra en otra carpeta.
try:
    from get_module import get_info
except:
    from .get_module import get_info

def get_types_info(lista_url: list):
    """
    lista_url: una lista con las direcciones web de la API que contiene la información del tipo a evaluar.\n
    Retorna una estructura de datos de Python (en este caso, lista) con la información del tipo.
    """
    return [get_info(url) for url in lista_url]

# Las siguientes funciones obtienen su información de la lista generada con get_types_info().
# De esta forma, evitamos hacer una nueva solictud GET cada vez que requerimos una información.
def nombre_tipos(lista_tipos: list):
    """
    lista_tipos: estructura de datos de la cual se obtiene la información.\n
    Accede, para cada uno de los tipos en la lista, hasta el nivel: API['name'].\n
    Retorna el nombre, en inglés, de los tipos contenidos en "lista_tipos".
    """
    resultado = [dict['name'] for dict in lista_tipos]
    return resultado

def relacion_dano(relacion: str, lista_tipos: list):
    """
    relacion: 'double_damage_from', 'double_damage_to', 'half_damage_from', 'half_damage_to', 'no_damage_from', 'no_damage_to'.
    lista_tipos: estructura de datos de la cual se obtiene la información.\n
    Accede, para cada uno de los tipos en la lista, hasta el nivel: API['damage_relations'][relacion][n(cada uno de los tipos de la relación)]['name'].\n
    Retorna un set con los nombres, en inglés, de los tipos de la relación.
    """
    numero_tipos = [dict['damage_relations'][relacion] for dict in lista_tipos]
    set_tipos = {tipo['name'] for bloque in numero_tipos for tipo in bloque}
    return set_tipos


if __name__ == '__main__':
    from get_base_info import poke_type, get_base_pokemon
    nombre = 'gengar'
    dict_base_pokemon = get_base_pokemon(nombre)
    lista_tipos = get_types_info(poke_type(dict_base_pokemon))

    print(f"Datos de {nombre.capitalize()}:")
    print(f"Es de tipo {nombre_tipos(lista_tipos)}.")
    print(f"Es súper efectivo contra los tipos {relacion_dano('double_damage_to', lista_tipos)}.")
    print(f"Es debil contra los tipos {relacion_dano('double_damage_from', lista_tipos)}.")
    print(f"Es resistente contra los tipos {relacion_dano('half_damage_from', lista_tipos)}.")
    print(f"Es poco eficaz contra los tipos {relacion_dano('half_damage_to', lista_tipos)}.")
    print(f"Es inmune contra los tipos {relacion_dano('no_damage_from', lista_tipos)}.")
    print(f"Es ineficaz contra los tipos {relacion_dano('no_damage_to', lista_tipos)}.")
    