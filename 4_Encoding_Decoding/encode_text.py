# Autor: Juan Angel Garza Castillo
# Matricula: 2007612

import base64
print('Bienvenido a codificadorBase64, en Python')

frase = input('Proporcione una frase que codificar: ')

frase_bytes = frase.encode('ascii')
base64_bytes = base64.b64encode(frase_bytes)
base64_message = base64_bytes.decode('ascii')

print('Resultado de su codificacion en Base64:', base64_message)