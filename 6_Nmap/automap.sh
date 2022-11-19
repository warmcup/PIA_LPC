#!/bin/bash
# Autor: Juan Angel Garza Castillo

echo =====Menu=====
echo '1. Escanear los hosts en una subred'
echo '2. Obtener detalles de un host'
echo '3. Escaneo UDP de un host'
echo '4. Escaneo por script de nmap'
echo '5. Salir'
read -p '>> ' opcion

case $opcion in
    1)
       read -p 'Subred: ' subnet
       nmap -sn $subnet -oN "subnet_scan_results.txt" > /dev/null 2>&1
    ;;
    2)
       read -p 'Host: ' host
       nmap -v -A $host -oN "host_details_results.txt" > /dev/null 2>&1
    ;;
    3)
       read -p 'Host: ' host
       nmap -sU $host -oN "host_udp_results.txt" > /dev/null 2>&1 --min-rate 5000
    ;;
    4)
       read -p 'Host: ' host
       read -p 'Script: ' script
       nmap --script $script $host -oN "host_${script}_results.txt" > /dev/null 2>&1
    ;;
    5)
       exit
    ;;
esac