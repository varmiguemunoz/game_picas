"""
Funcion que retorna el resultado de la pica
"""

def generate_picas(key, try_number):
    picas = 0
    fijas = 0

    for i in range(4):
        if try_number[i] == key[i]:
            fijas += 1
        elif try_number[i] in key:
            picas += 1


    return picas, fijas
