# Dada la organización en diferentes carpetas, la siguiente importación presenta 2 alternativas:
# La primera (en "try"), una importación absoluta, permite correr el código desde este script.
# La segunda forma (en "except"), una importación relativa, permite que el código corra desde un script que se encuentra en otra carpeta.
try:
    from data import validacion_pokemon
except:
    from .data import validacion_pokemon

# La función "open(x, 'r')" transforma el archivo en la ruta "x" en un objeto string.
# En este caso, se ingresa un documento .txt con los nombres en inglés de todos los pokémon.
# El string generado anteriormente se ordena como una lista de nombres.
with open("./assets/txt/pokemon_list.txt", "r") as f:
    pokemon_lista = f.readlines()   
pokemon_lista = [elemento.strip('\n') for elemento in pokemon_lista]

def validate(name: str, p_l: str = pokemon_lista, mensaje: str = validacion_pokemon):
    """
    name: string con nombre del pokémon.
    p_l: string con los nombres válidos.
    mensaje: string con una advertencia de que el valor "name" no se encuentra en "p_l".\n
    Excepción: Si el nombre del pokémon es "codigo-cero", automáticamente le asigna el valor "type-null".\n
    Retorna el nombre, una vez validado.
    """
    if name =='codigo-cero':
        name = 'type-null'
    while name not in p_l:
        name = input(mensaje).lower()
    return name


if __name__ == '__main__':
    name = 'codigo-cero'
    print(validate(name))
