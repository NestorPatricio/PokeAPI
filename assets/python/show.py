import webbrowser
import os
import time
# Las siguientes importacioes podrían ser usadas en otro proyecto:
#from get_evo import get_evolution
#from build_evo_html import build_evo_html

def show_pics(html: str, nombre: str):
    """
    html: un string que debe ser convertido a archivo HTML.
    nombre: un string con el nombre del archivo HTML.\n
    El archivo se abrirá, automáticamente, en el navegador predeterminado.
    Posteriormente, el archivo se elimina de la memoria.\n
    No tiene retorno.
    """
    with open(f'{nombre}.html','w', encoding='utf-8') as f:
        f.write(html)
    print(f'La información de {nombre.capitalize()} se mostrará en tu Navegador...')
    time.sleep(2)
    webbrowser.open(f'{nombre}.html')
    time.sleep(5)
    os.remove(f'{nombre}.html')
    

if __name__ == '__main__':
    from build_pokemon_html import build_html
    nombre = "mew"
    html = build_html(nombre)
    show_pics(html, nombre)