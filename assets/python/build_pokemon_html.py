from string import Template
# Dada la organización en diferentes carpetas, las siguientes importaciones presentan 2 alternativas.
# La primera (en "try"), una importación absoluta, permite correr el código desde este script.
# La segunda forma (en "except"), una importación relativa, permite que el código corra desde un script que se encuentra en otra carpeta.
try:
    from get_base_info import get_base_pokemon, poke_name, poke_num, poke_weight, poke_height, poke_type, poke_stats, poke_photo
except:
    from .get_base_info import get_base_pokemon, poke_name, poke_num, poke_weight, poke_height, poke_type, poke_stats, poke_photo
try:
    from get_types import get_types_info, nombre_tipos, relacion_dano
except:
    from .get_types import get_types_info, nombre_tipos, relacion_dano
try:
    from get_species_info import get_species, indicadores, preevolucion, descripciones
except:
    from .get_species_info import get_species, indicadores, preevolucion, descripciones
try:
    from data import TIPOS
except:
    from .data import TIPOS

# La función "open(x, 'r', encoding = 'utf-8)" transforma el archivo x en un objeto string.
# El valor "encoding = 'utf-8'" permite que se entiendan caracteres especiales.
with open('./assets/html/input.html', 'r', encoding = 'utf-8') as archivo:
    html = archivo.read()


def tipos(datos: list):
    """
    datos: estructura de datos que contiene el nombre, en inglés, con los tipos del pokémon.\n
    Se genera una etiqueta de HTML <span>.
    Dentro del atributo "class" se ingresa el tipo del pokémon en inglés, el cual está asociado a un estilo en CSS.
    Dentro de la etiqueta se produce la traducción al español, con la primera letra en mayúscula.\n
    Retorna un objeto string con todas las etiquetas <span> construidas. 
    """
    conjunto = ""
    for tipo in datos:
        conjunto += f'<span class="label {tipo}">{TIPOS[tipo].capitalize()}</span>'
    return conjunto

def indicador(valor: str):
    """
    valor: 'Legendario', 'Mítico', Bebé'.\n
    Retorna una etiqueta <span> con el valor del parámetro "valor".
    """
    return f'<span class="label other">{valor}</span>'

def build_html(name: str):
    """
    name: nombre de un pokémon. Objeto string que sirve como plantilla.\n
    Retorna un string con el Template completado.
    """
    entrada = Template(html)
    dict_base_pokemon = get_base_pokemon(name)
    lista_tipos = get_types_info(poke_type(dict_base_pokemon))
    dict_species = get_species(poke_num(dict_base_pokemon))

    preevolution = f"<h4>Etapa previa: {preevolucion(dict_species)}.</h4>"
    
    legendario = indicadores('legendary', dict_species)
    mitico = indicadores('mythical', dict_species)
    bebe = indicadores('baby', dict_species)

    salida = entrada.substitute(
        Nombre = poke_name(dict_base_pokemon),
        Numero = poke_num(dict_base_pokemon),
        Preevolucion = preevolution if preevolucion(dict_species) != None else '',
        Peso = poke_weight(dict_base_pokemon),
        Talla = poke_height(dict_base_pokemon),
        Foto = poke_photo(dict_base_pokemon),
        HP = poke_stats(0, dict_base_pokemon),
        Ataque = poke_stats(1, dict_base_pokemon),
        Defensa = poke_stats(2, dict_base_pokemon),
        AtaqSp = poke_stats(3, dict_base_pokemon),
        DefenSp = poke_stats(4, dict_base_pokemon),
        Velocidad = poke_stats(5, dict_base_pokemon),
        Tipos = tipos(nombre_tipos(lista_tipos)),
        Legendario = indicador('Legendario') if legendario == True else '',
        Mitico = indicador('Mítico') if mitico == True else '', 
        Bebe = indicador('Bebé') if bebe == True else '',
        Descripcion = descripciones(dict_species),
        Efectivo = tipos(relacion_dano('double_damage_to', lista_tipos)),
        Debil = tipos(relacion_dano('double_damage_from', lista_tipos)),
        Resistente = tipos(relacion_dano('half_damage_from', lista_tipos)),
        PocoEficaz = tipos(relacion_dano('half_damage_to', lista_tipos)),
        Inmune = tipos(relacion_dano('no_damage_from', lista_tipos)),
        Ineficaz = tipos(relacion_dano('no_damage_to', lista_tipos))
    )
    resultado = salida
    return resultado


if __name__ == '__main__':
    name = 'articuno'
    print(build_html(name))