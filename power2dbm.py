#!/usr/bin/env python
# -*- coding: utf-8 -*

from math import log10
from pick import pick

# print(option,index)

'''
 Funciones de conversion:
'''

def mw_to_dbm(mW):
    """This function converts a power given in mW to a power given in dBm."""
    return 10.*log10(mW)

def dbm_to_mw(dBm):
    """This function converts a power given in dBm to a power given in mW."""
    return 10**((dBm)/10.)


def main():
    try:
        title = 'Conversor de nivel de potencia (dBm <--> mW): '
        options = ['1) mW to dBm', '2) dBm to mW']
        option, index = pick(options, title, indicator='=>', default_index=0)

        if index == 0:
            data = input("Introduce un valor en mW: ")
            print "%.2f mW equivale a %.2f dBm" % (data, mw_to_dbm(data))

        elif index == 1:
            data = input("Introduce un valor en dBm: ")
            print "%.2f dBm equivale a %.2f mW" % (data, dbm_to_mw(data))
        else:
            print "Ninguna de las anteriores"
    except Exception as e:
        print e.message
        return 1 # indicates error, but not necessary
    else:
        return 0 # return 0 # indicates errorlessly exit, but not necessary

# Main function call
if __name__ == '__main__':
    # sys.exit(main(sys.argv)) # used to give a better look to exists
    main()
