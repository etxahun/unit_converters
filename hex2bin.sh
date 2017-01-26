#!/bin/bash

GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -en "${GREEN} Introduce un número en HEX: ${NC} "
read HEX1

echo -ne "${GREEN} El valor de ${CYAN}$HEX1 ${GREEN}en binario vale: ${YELLOW}"
echo "ibase=16;obase=2;$HEX1" | bc
