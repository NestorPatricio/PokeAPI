import webbrowser
import os
import time
#from get_evo import get_evolution
#from build_evo_html import build_evo_html

def show_pics(html, nombre):
    with open(f'{nombre}.html','w', encoding='utf-8') as f:
        f.write(html)
    print(f'La información de {nombre.capitalize()} se mostrará en tu Navegador...')
    time.sleep(2)
    webbrowser.open(f'{nombre}.html')
    time.sleep(5)
    os.remove(f'{nombre}.html')
    

if __name__ == '__main__':
    from build_pokemon_html import build_html
    nombre = "charizard"
    html = build_html(nombre)
    show_pics(html, nombre)