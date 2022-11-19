#!/bin/bash
# Script portscanv1.sh
# 27/Sep/2022 - Juan Angel Garza Castillo
#
# Ejemplo de Menu en BASH
#
date
	echo "------------------------"
	echo "     Menu Principal"
	echo "------------------------"
	echo "1. Net Discover"
	echo "2. Portscanv1"
	echo "3. Welcome"
	echo "4. Exit"
read -p "Opcion [ 1 - 4 ] " c
case $c in
	1) ./netdiscover.sh;;
	2) ./portscanv1.sh;;
	3) ./welcome.sh;; 
	4) exit 0;;
esac