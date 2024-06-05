"""
Hook encargado de generar un numero aleatorio ⚡️
"""

import random

# Funcion para retornar un numero aleatorio
def generate_number():
    digits = random.sample(range(10), 4)
    return digits
