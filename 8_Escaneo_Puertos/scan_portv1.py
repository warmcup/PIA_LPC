# Autor: Juan Angel Garza Castillo
# Matricula: 2007612

import sys
from socket import *

host = sys.argv[1]
portstrs = sys.argv[2].split('-')

start_port = int(portstrs[0])
end_port = int(portstrs[1])

target_ip = gethostbyname(host)
opened_ports = []

# Sumado 1 a end_port para hacer al intervalo inclusivo
for port in range(start_port, end_port + 1):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0 :
        opened_ports.append(port)

print('Puertos abiertos: ')
for i in opened_ports:
    print(i)