# Autor: Juan Angel Garza Castillo
# Matricula: 2007612

import socket

def scan(addr, port):
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = socket_obj.connect_ex((addr, port))
    socket_obj.close()
    return result


ports = [21, 22, 25, 80]

for i in range(1, 256):
    addr = '192.168.226.{}'.format(i)
    for port in ports:
        res = scan(addr, port)
        if res == 0:
            print(addr, port, 'OK')
        else:
            print(addr, port, 'Fail')