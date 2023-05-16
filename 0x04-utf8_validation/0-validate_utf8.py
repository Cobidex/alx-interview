#!/usr/bin/python3
'''
This module contains the validUTF8 method
'''


def validUTF8(data):
    '''
    determines if a given data set represents a valid UTF-8 encoding
    '''
    cont_bytes = 0
    for byte in data:
        if cont_bytes:
            if byte >> 6 != 0b10:
                return False
            cont_bytes -= 1
        else:
            if byte >> 7 == 0b0:
                pass
            elif byte >> 5 == 0b110:
                cont_bytes = 1
            elif byte >> 4 == 0b1110:
                cont_bytes = 2
            elif byte >> 3 == 0b11110:
                cont_bytes = 3
            else:
                return False

    if cont_bytes:
        return False
    return True
