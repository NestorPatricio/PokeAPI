from time import sleep
from assets.python.poke_validation import validate
from assets.python.validate import validador
from assets.python.show import show_pics
from assets.python.build_pokemon_html import build_html
import assets.python.data as d
import os
import sys

# Esta variable genera el valor que irá dentro de la función os.system().
# Con esto, se limpia la pantalla de la terminal, como si de un cambio de pa´gina se tratase.
clear = 'cls' if sys.platform == 'win32' else 'clear'

# El ciclo while permite que el programa no termine al hacer su trabajo, sino que vuelve al inicio.
# Dentro se establecen tiempos de espera con sleep(), para permitir la lectura de la información.
while True:
    os.system(clear)
    opcion = input(d.MENU)

    # Acá se evalúa que la opción ingresada sea válida.
    opcion = validador(['0', '1'], opcion)

    # Presenta las instrucciones para poder mostrar la información.
    if opcion == '1':
        os.system(clear)
        name = input(d.ELECCION)

        # Acá se evalúa que la opción ingresada sea válida.
        name = validate(name.lower())
        print(d.ESPERA)
        
        # Se genera un string correspondiente al HTML con la información del pokémon.
        # Ese string se convierte en un archivo .html válido, y lo abre en el navegador.
        html = build_html(name)
        show_pics(html, name)
        sleep(3)

    # En caso de no querer continuar, acá se despide y se sale del programa.
    else:
        print('No hay problema. Puedes volver cuando quieras.')
        sleep(2)
        os.system(clear)
        exit()