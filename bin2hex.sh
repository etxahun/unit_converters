#!/bin/bash

GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -en "${GREEN} Introduce un número en Binario: ${NC}"
read BIN1
printf  "${GREEN} El valor hexadecimal de ${CYAN}$BIN1 ${GREEN}es:${NC} ${YELLOW}%x\n" "$((2#$BIN1))"
