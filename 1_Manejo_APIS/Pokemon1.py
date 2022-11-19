# Autor: Juan Ángel Garza Castillo
# Matrícula: 2007612

import requests

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form'
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        payload = respuesta.json()
        resultados = payload.get('results', [])
        if resultados:
            for pokemon in resultados:
                print(pokemon['name'])