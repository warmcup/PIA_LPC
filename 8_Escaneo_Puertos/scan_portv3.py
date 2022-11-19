# Autor: Juan Angel Garza Castillo
# Matricula: 2007612

import sys
import threading
from socket import *


def tcp_test(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0 :
        print('Puerto abierto:', port)

if __name__ == '__main__':
    host = sys.argv[1]
    portstrs = sys.argv[2].split('-')

    start_port = int(portstrs[0])
    end_port = int(portstrs[1])

    target_ip = gethostbyname(host)
    
    hilos = []
    # Sumado 1 a end_port para hacer al intervalo inclusivo
    for port in range(start_port, end_port + 1):
        hilo = threading.Thread(target = tcp_test, args = (port,))
        hilos.append(hilo)
        hilo.start()