import requests
import json

def get_info(url: str):
    """
    url: dirección web de una API.\n
    Realiza una solicitud GET a "url".\n
    Retorna una estructura de datos de Python.
    """
    return json.loads(requests.get(url).text)


if __name__ == '__main__':
    url = f'https://pokeapi.co/api/v2/pokemon/charmander'
    print(get_info(url))
