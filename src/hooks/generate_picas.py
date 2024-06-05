"""
Funcion que retorna el resultado de la pica
"""

def generate_picas(key, try_number):
    picas = 0
    fijas = 0

    key_str = str(key)  # Convertir el número clave a una cadena para facilitar la comparación

    for i in range(4):
        digit_try = try_number % 10
        try_number //= 10

        if str(digit_try) == key_str[i]:  # Comparar el dígito de intento con el dígito correspondiente del número clave
            fijas += 1
        elif str(digit_try) in key_str:  # Verificar si el dígito de intento está presente en el número clave, pero en una posición diferente
            picas += 1

    return picas, fijas
