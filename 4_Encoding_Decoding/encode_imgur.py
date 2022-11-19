# Autor: Juan Angel Garza Castillo
# Matricula: 2007612

import requests, base64
from requests import Response


if __name__ == '__main__':
    url = 'https://i.imgur.com/xwy9YBa.jpeg'
    Response: Response = requests.get(url, stream=True)
    with open('gato.jpeg', 'wb') as file_down:
        for chunk in Response.iter_content():
            file_down.write(chunk)
    Response.close()
    with open('gato.jpeg', 'rb') as bin_file:
        b_data = bin_file.read()
        b64_data = base64.b64encode(b_data)
        b64_message = b64_data.decode('utf8')
        print(b64_message)
