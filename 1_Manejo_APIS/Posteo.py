# Autor: Juan Ángel Garza Castillo
# Matrícula: 2007612

import requests

if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    args = {'nombre' : 'Gerardo', 'matricula' : '2007612', 'curso' : 'Programacion para ciberseguridad'}
    respuesta = requests.post(url, params=args)
    if respuesta.status_code == 200:
        print(respuesta.content)