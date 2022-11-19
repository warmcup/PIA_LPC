# Autor: Juan Angel Garza Castillo
# Matricula: 2007612

from ftplib import FTP

# Definimos nuestra conexión
with FTP('192.168.226.133') as ftp:

    # Nos autenticamos con usuario/contraseña
    ftp.login('johnny', '2007612')
    
    # Cambiamos al directorio en que el usuario tiene permisos
    ftp.cwd('upload')

    # Cargamos un archivo modificado
    with open('ADVERTENCIA.txt', 'rb') as file:
        ftp.storlines('STOR ADVERTENCIA.txt', file)
