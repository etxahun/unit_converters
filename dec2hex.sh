#!/bin/bash

GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo  -en "${GREEN} Introduce un número en DEC: ${NC}"
read DEC1
printf  "${GREEN} El valor hexadecimal de ${CYAN}$DEC1 ${GREEN}es:${NC} ${YELLOW}%x\n" $DEC1 


