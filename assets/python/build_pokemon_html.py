from string import Template
try:
    import get_base_info
except:
    from . import get_base_info
try:
    import get_types
except:
    from . import get_types
try:
    import get_species_info
except:
    from . import get_species_info
try:
    import data as d
except:
    from . import data as d

with open('./assets/html/input.html', 'r', encoding = 'utf-8') as archivo:
    html = archivo.read()

def tipos(datos):
    conjunto = ""
    for tipo in datos:
        conjunto += f'<span class="label {tipo}">{d.TIPOS[tipo].capitalize()}</span>'
    return conjunto

def indicador(valor):
    """ valor: 'Legendario', 'Mítico', Bebé'
    """
    return f'<span class="label other">{valor}</span>'

def build_html(name):
    entrada = Template(html)
    dict_base_pokemon = get_base_info.get_base_pokemon(name)
    lista_tipos = get_types.get_types_info(get_base_info.poke_type(dict_base_pokemon))
    dict_species = get_species_info.get_species(get_base_info.poke_num(dict_base_pokemon))

    preevolucion = f"<h4>Etapa previa: {get_species_info.preevolucion(dict_species)}.</h4>"
    
    legendario = get_species_info.indicadores('legendary', dict_species)
    mitico = get_species_info.indicadores('mythical', dict_species)
    bebe = get_species_info.indicadores('baby', dict_species)

    salida = entrada.substitute(
        Nombre = get_base_info.poke_name(dict_base_pokemon),
        Numero = get_base_info.poke_num(dict_base_pokemon),
        Preevolucion = preevolucion if get_species_info.preevolucion(dict_species) != None else '',
        Peso = get_base_info.poke_weight(dict_base_pokemon),
        Talla = get_base_info.poke_height(dict_base_pokemon),
        Foto = get_base_info.poke_photo(dict_base_pokemon),
        HP = get_base_info.poke_stats(0, dict_base_pokemon),
        Ataque = get_base_info.poke_stats(1, dict_base_pokemon),
        Defensa = get_base_info.poke_stats(2, dict_base_pokemon),
        AtaqSp = get_base_info.poke_stats(3, dict_base_pokemon),
        DefenSp = get_base_info.poke_stats(4, dict_base_pokemon),
        Velocidad = get_base_info.poke_stats(5, dict_base_pokemon),
        Tipos = tipos(get_types.nombre_tipos(lista_tipos)),
        Legendario = indicador('Legendario') if legendario == True else '',
        Mitico = indicador('Mítico') if mitico == True else '', 
        Bebe = indicador('Bebé') if bebe == True else '',
        Descripcion = get_species_info.descripciones(dict_species),
        Efectivo = tipos(get_types.relacion_dano('double_damage_to', lista_tipos)),
        Debil = tipos(get_types.relacion_dano('double_damage_from', lista_tipos)),
        Resistente = tipos(get_types.relacion_dano('half_damage_from', lista_tipos)),
        PocoEficaz = tipos(get_types.relacion_dano('half_damage_to', lista_tipos)),
        Inmune = tipos(get_types.relacion_dano('no_damage_from', lista_tipos)),
        Ineficaz = tipos(get_types.relacion_dano('no_damage_to', lista_tipos))
    )
    resultado = salida
    return resultado


if __name__ == '__main__':
    name = 'articuno'
    print(build_html(name))