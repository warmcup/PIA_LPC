# Autor: Juan Angel Garza Castillo
# Matricula: 2007612

import os
import nmap

scanner = nmap.PortScanner()

# El argumento --min-parallelism 200 se utiliza para incrementar
# la cantidad de threads empleadas en el scan

# nmap -sU ; escanea en modo UDP
def udpScan(subnet):
    scanner.scan(subnet, None, '-sU --min-parallelism 200')
    hosts = scanner.all_hosts()
    if hosts:
        print('Resultados del scan:')
    else:
        print('Sin resultados')
    for host in hosts:
        print('= Host online:', host + ' =')
        for port in scanner[host]['udp'].keys():
            if scanner[host]['udp'][port]['state'] != 'closed':
                print('Puerto: {} ; estado: {}'.format(port, scanner[host]['udp'][port]['state']))
        print()

# nmap -sSU ; escanea en modo SYN y UDP
def fullScan(subnet):
    scanner.scan(subnet, None, '-sSU --min-parallelism 200')
    hosts = scanner.all_hosts()
    if hosts:
        print('Resultados del scan:')
    else:
        print('Sin resultados')
    for host in hosts:
        print('= Host online:', host + ' =')
        protos = scanner[host].all_protocols()
        for proto in protos:
            print('Protocolo:', proto)
            for port in scanner[host][proto].keys():
                print('Puerto: {} ; estado: {}'.format(port, scanner[host][proto][port]['state']))
        print()

# nmap -O ; detecta sistema operativo
def osScan(subnet):
    scanner.scan(subnet, None, '-O --min-parallelism 200')
    hosts = scanner.all_hosts()
    if hosts:
        print('Resultados del scan:')
    else:
        print('Sin resultados')
    for host in hosts:
        print('= Host online:', host + ' =')
        osInfo = scanner[host]['osmatch']
        if osInfo:
            print('SO detectado:', osInfo[0]['name'], '; Certeza:', osInfo[0]['accuracy'] + '%')
        else:
            print('No se pudo determinar un posible SO para el host')
        print()
        
# nmap -sN ; omite escaneo de puertos
def netEchoScan(subnet):
    scanner.scan(subnet, None, '-sN --min-parallelism 200')
    hosts = scanner.all_hosts()
    if hosts:
        print('Resultados del scan:')
    else:
        print('Sin resultados')
    for host in hosts:
        print('= Host online:', host + ' =')
        print()

# Menu
def main():
    os.system('cls')
    print('Menu')
    print('1. Escaneo UDP')
    print('2. Escaneo completo (TCP/UDP)')
    print('3. Deteccion de SO')
    print('4. Escaneo con ping')
    print('Ingrese una opcion')
    op = input('> ')
    while op not in [str(n) for n in range(1, 5)]:
        print('Escoja una opcion valida')
        op = input('> ')
    print('Ingrese el host/subred a escanear')
    target = input('> ')
    match op:
        case '1':
            udpScan(target)
        case '2':
            fullScan(target)
        case '3':
            osScan(target)
        case '4':
            netEchoScan(target)

if __name__ == '__main__':
    main()