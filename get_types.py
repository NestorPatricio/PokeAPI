from get_module import get_info
try:
    from .assets.python.data import TIPOS
except:
    from assets.python.data import TIPOS

def get_types_info(lista_url):
    return [get_info(url) for url in lista_url]

def nombre_tipos(lista_tipos):
    resultado = [dict['name'] for dict in lista_tipos]
    return resultado

def relacion_dano(relacion, lista_tipos):
    """
    relacion: 'double_damage_from', 'double_damage_to', 'half_damage_from', 'half_damage_to', 'no_damage_from', 'no_damage_to'.
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
    