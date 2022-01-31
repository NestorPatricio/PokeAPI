from time import sleep
from assets.python.poke_validation import validate
from assets.python.validate import validador
from assets.python.show import show_pics
from assets.python.build_pokemon_html import build_html
import assets.python.data as d
import os
import sys

clear = 'cls' if sys.platform == 'win32' else 'clear'

while True:
    os.system(clear)
    opcion = input(d.MENU)
    opcion = validador(['0', '1'], opcion)

    if opcion == '1':
        os.system(clear)
        name = input(d.ELECCION)
        name = validate(name.lower())
        print(d.ESPERA)
        
        html = build_html(name)
        show_pics(html, name)
        sleep(3)

    else:
        print('No hay problema. Puedes volver cuando quieras.')
        sleep(2)
        os.system(clear)
        exit()