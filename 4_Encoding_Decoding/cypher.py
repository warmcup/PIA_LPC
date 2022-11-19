# Autor: Juan Angel Garza Castillo
# Matricula: 2007612

from cryptography.fernet import Fernet

def gen_write():
    key = Fernet.generate_key()
    with open('pass.key', 'wb') as k:
        k.write(key)

def call_key():
    return open('pass.key', 'rb').read()

gen_write()
key = call_key()
msg = 'Esto es una prueba del cifrado con el modulo cryptography'.encode()
a = Fernet(key)
ciphered = a.encrypt(msg)
print(ciphered)

key = call_key()
b = Fernet(key)
deciphered = b.decrypt(ciphered)
print(deciphered)