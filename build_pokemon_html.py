from string import Template
import get_base_info
import get_types
import get_species_info
try:
    from .assets.python import data
except:
    from assets.python import data

"""
def tipos(datos):
        secuencia = []
        for tipo in datos:
            secuencia = f'<span class="label {tipo}">{data.TIPOS[tipo].capitalize()}</span>'
        return secuencia"""

def build_html(name):
    entrada = Template("""<!DOCTYPE html>
<html lang="es" dir="ltr">

<head>

    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="stylesheet" href="./assets/css/mystyle.css">
    <title>$Nombre</title>
    <link rel="shortcut icon" type="image/png" href="./assets/img/favicon.png">
    <!--<meta> informativos para que tu página sea fácil de encontrar por los buscadores.-->
    <meta name="author" content="Néstor Patricio Rojas Ríos">
    <meta name="description" content="Información del pokémon $Nombre">
    <meta name="keywords" content="pokemon, pokedex">

</head>

<body>

    <div class="column2">
        <div class="card">
            <h1>#$Numero $Nombre</h1>
            <img src="$Foto" width="200" height="200">
            <div class="container">
                $Preevolucion
                <h2>Estadísticas</h2>
                <table>
                    <tr>
                        <td>
                            <h5>HP: $HP</h5>
                        </td>
                        <td>
                            <h5>Ataque: $Ataque</h5>
                        </td>
                        <td>
                            <h5>Defensa: $Defensa</h5>
                        </td>
                        <td>
                            <h5>Ataque Especial: $AtaqSp</h5>
                        </td>
                        <td>
                            <h5>Defensa Especial: $DefenSp</h5>
                        </td>
                        <td>
                            <h5>Velocidad: $Velocidad</h5>
                        </td>
                    </tr>
                </table>
                <h3><b>Tipo</b></h3>
                $Tipos

                <p>$Descripcion</p>

                <h3>Super efectivo contra:</h3>
                $Efectivo
                <h3>Débil contra:</h3>
                $Debil
                <h3>Resistente contra:</h3>
                $Resistente
                <h3>Poco Eficaz contra</h3>
                $PocoEficaz
                <h3>Inmune contra:</h3>
                $Inmune
                <h3>Ineficaz contra:</h3>
                $Ineficaz

            </div>
        </div>

</body>

</html>""")
    dict_base_pokemon = get_base_info.get_base_pokemon(name)
    lista_tipos = get_types.get_types_info(get_base_info.poke_type(dict_base_pokemon))
    dict_species = get_species_info.get_species(name)

    preevolucion = f"<h4>Etapa previa: {get_species_info.preevolucion(dict_species)}.</h4>"
    
    def tipos(datos):
        conjunto = []
        for tipo in datos:
            conjunto.append(f'<span class="label {tipo}">{data.TIPOS[tipo].capitalize()}</span>')
        return conjunto

    salida = entrada.substitute(
        Nombre = get_base_info.poke_name(dict_base_pokemon),
        Numero = get_base_info.poke_num(dict_base_pokemon),
        Preevolucion = preevolucion if get_species_info.preevolucion(dict_species) != None else '',
        Foto = get_base_info.poke_photo(dict_base_pokemon),
        HP = get_base_info.poke_stats(0, dict_base_pokemon),
        Ataque = get_base_info.poke_stats(1, dict_base_pokemon),
        Defensa = get_base_info.poke_stats(2, dict_base_pokemon),
        AtaqSp = get_base_info.poke_stats(3, dict_base_pokemon),
        DefenSp = get_base_info.poke_stats(4, dict_base_pokemon),
        Velocidad = get_base_info.poke_stats(5, dict_base_pokemon),
        Tipos = tipos(get_types.nombre_tipos(lista_tipos)),
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
    name = 'larvitar'
    print(build_html(name))