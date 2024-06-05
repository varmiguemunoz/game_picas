"""
Entry point del programa ⚡️
"""

from hooks.generate_number import generate_number
from hooks.generate_picas import generate_picas
from hooks.generate_message import generate_message

def video_game():
    key = generate_number()
    tries = 0
    max_tries = 12

    print(key)

    while tries < max_tries:
        user =  input("Ingresa tu intento: ")
        tries += 1

        if len(user) != 1:
            print("Asegúrate de ingresar un numero correctamente.")
            continue

        picas, fijas = generate_picas(key, int(user))
        print(picas)
        print(fijas)

        if fijas == 4:
            print(generate_message(tries))
            break
        else:
            print(f"Intentos: {tries}, picas: {picas}, fijas:{fijas}")


        if tries == max_tries:
            print(generate_message(tries))


def main():
    print("Iniciando el juego")
    video_game()


if __name__ == "__main__":
    main()
